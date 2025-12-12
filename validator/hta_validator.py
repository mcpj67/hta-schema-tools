#!/usr/bin/env python3
"""
HTA Schema Validator v0.1
Simple validator for HTA Schema models demonstrating structural and semantic checks
"""

import json
import sys
from typing import Dict, List, Tuple, Set
from pathlib import Path


class HTASchemaValidator:
    """Validator for HTA Schema v0.1 models"""
    
    def __init__(self, schema_path: str = None, model_path: str = None):
        self.schema = None
        self.model = None
        self.errors = []
        self.warnings = []
        
        if schema_path:
            self.load_schema(schema_path)
        if model_path:
            self.load_model(model_path)
    
    def load_schema(self, path: str):
        """Load JSON Schema definition"""
        with open(path, 'r') as f:
            self.schema = json.load(f)
    
    def load_model(self, path: str):
        """Load HTA model to validate"""
        with open(path, 'r') as f:
            self.model = json.load(f)
    
    def validate(self) -> Tuple[bool, List[str], List[str]]:
        """
        Run all validation checks
        Returns: (is_valid, errors, warnings)
        """
        self.errors = []
        self.warnings = []
        
        if not self.model:
            self.errors.append("No model loaded")
            return False, self.errors, self.warnings
        
        # Run validation checks
        self._validate_structure()
        self._validate_tree_properties()
        self._validate_probabilities()
        self._validate_parameter_references()
        self._validate_parameter_ranges()
        
        is_valid = len(self.errors) == 0
        return is_valid, self.errors, self.warnings
    
    def _validate_structure(self):
        """Check basic structural requirements"""
        required_fields = ['schema_version', 'model_metadata', 'model_structure', 
                          'parameters', 'analysis_settings']
        
        for field in required_fields:
            if field not in self.model:
                self.errors.append(f"Missing required field: {field}")
        
        # Check schema version
        if 'schema_version' in self.model:
            version = self.model['schema_version']
            if not version.startswith('0.1.'):
                self.warnings.append(f"Schema version {version} may not match validator version 0.1")
        
        # Check model type
        if 'model_metadata' in self.model:
            model_type = self.model['model_metadata'].get('model_type')
            if model_type != 'decision_tree':
                self.errors.append(f"Model type '{model_type}' not supported in v0.1 (only 'decision_tree')")
    
    def _validate_tree_properties(self):
        """Validate decision tree structural properties"""
        if 'model_structure' not in self.model:
            return
        
        structure = self.model['model_structure']
        nodes = structure.get('nodes', {})
        root_id = structure.get('root_node')
        
        if not root_id:
            self.errors.append("No root_node specified")
            return
        
        if root_id not in nodes:
            self.errors.append(f"Root node '{root_id}' not found in nodes")
            return
        
        # Check root is decision node
        root_node = nodes[root_id]
        if root_node.get('node_type') != 'decision':
            self.errors.append(f"Root node must be 'decision' type, got '{root_node.get('node_type')}'")
        
        # Check for cycles using DFS
        visited = set()
        rec_stack = set()
        
        def has_cycle(node_id: str) -> bool:
            visited.add(node_id)
            rec_stack.add(node_id)
            
            node = nodes.get(node_id)
            if not node:
                return False
            
            branches = node.get('branches', [])
            for branch in branches:
                target = branch.get('target_node')
                if target:
                    if target not in visited:
                        if has_cycle(target):
                            return True
                    elif target in rec_stack:
                        return True
            
            rec_stack.remove(node_id)
            return False
        
        if has_cycle(root_id):
            self.errors.append("Model contains cycles (not a valid tree)")
        
        # Check all nodes are reachable from root
        reachable = self._get_reachable_nodes(root_id, nodes)
        unreachable = set(nodes.keys()) - reachable
        if unreachable:
            self.warnings.append(f"Unreachable nodes: {unreachable}")
        
        # Check all paths terminate
        terminal_count = sum(1 for n in nodes.values() if n.get('node_type') == 'terminal')
        if terminal_count == 0:
            self.errors.append("No terminal nodes found - all paths must terminate")
    
    def _get_reachable_nodes(self, start: str, nodes: Dict) -> Set[str]:
        """Get set of all nodes reachable from start node"""
        reachable = set()
        stack = [start]
        
        while stack:
            node_id = stack.pop()
            if node_id in reachable:
                continue
            reachable.add(node_id)
            
            node = nodes.get(node_id)
            if node:
                for branch in node.get('branches', []):
                    target = branch.get('target_node')
                    if target and target not in reachable:
                        stack.append(target)
        
        return reachable
    
    def _validate_probabilities(self):
        """Check that probabilities sum to 1.0 for chance nodes"""
        if 'model_structure' not in self.model:
            return
        
        nodes = self.model['model_structure'].get('nodes', {})
        parameters = self.model.get('parameters', {})
        
        tolerance = 1e-4
        
        for node_id, node in nodes.items():
            if node.get('node_type') != 'chance':
                continue
            
            branches = node.get('branches', [])
            prob_sum = 0.0
            prob_refs = []
            
            for branch in branches:
                prob_ref = branch.get('probability', {}).get('parameter_ref')
                if prob_ref:
                    prob_refs.append(prob_ref)
                    param = parameters.get(prob_ref)
                    if param:
                        prob_sum += param.get('base_value', 0.0)
                    else:
                        self.errors.append(f"Parameter '{prob_ref}' referenced but not defined")
            
            if abs(prob_sum - 1.0) > tolerance:
                self.errors.append(
                    f"Probabilities in chance node '{node_id}' sum to {prob_sum:.6f}, should be 1.0"
                    f"\n  Parameters: {prob_refs}"
                )
    
    def _validate_parameter_references(self):
        """Check all parameter references resolve to defined parameters"""
        if 'model_structure' not in self.model or 'parameters' not in self.model:
            return
        
        nodes = self.model['model_structure'].get('nodes', {})
        parameters = self.model.get('parameters', {})
        
        referenced = set()
        
        # Collect all parameter references
        for node in nodes.values():
            # Check branches
            for branch in node.get('branches', []):
                # Probability references
                prob_ref = branch.get('probability', {}).get('parameter_ref')
                if prob_ref:
                    referenced.add(prob_ref)
                # Cost references
                cost_ref = branch.get('initial_cost', {}).get('parameter_ref')
                if cost_ref:
                    referenced.add(cost_ref)
            
            # Check outcomes (terminal nodes)
            outcomes = node.get('outcomes', {})
            if outcomes:
                for cost_item in outcomes.get('costs', []):
                    cost_ref = cost_item.get('value', {}).get('parameter_ref')
                    if cost_ref:
                        referenced.add(cost_ref)
                    duration_ref = cost_item.get('duration_years', {}).get('parameter_ref')
                    if duration_ref:
                        referenced.add(duration_ref)
                
                for util_item in outcomes.get('utilities', []):
                    util_ref = util_item.get('value', {}).get('parameter_ref')
                    if util_ref:
                        referenced.add(util_ref)
                    duration_ref = util_item.get('duration_years', {}).get('parameter_ref')
                    if duration_ref:
                        referenced.add(duration_ref)
                
                life_years_ref = outcomes.get('life_years', {}).get('parameter_ref')
                if life_years_ref:
                    referenced.add(life_years_ref)
        
        # Check all references exist
        for ref in referenced:
            if ref not in parameters:
                self.errors.append(f"Referenced parameter '{ref}' not defined in parameters section")
        
        # Warn about unused parameters
        defined = set(parameters.keys())
        unused = defined - referenced
        if unused:
            self.warnings.append(f"Unused parameters (not referenced in model): {unused}")
    
    def _validate_parameter_ranges(self):
        """Check parameter values are within reasonable ranges"""
        if 'parameters' not in self.model:
            return
        
        parameters = self.model['parameters']
        
        for param_id, param in parameters.items():
            param_type = param.get('type')
            base_value = param.get('base_value')
            
            if base_value is None:
                continue
            
            # Type-specific range checks
            if param_type == 'probability':
                if not (0.0 <= base_value <= 1.0):
                    self.errors.append(
                        f"Parameter '{param_id}' (type: probability) has base_value {base_value} "
                        "outside valid range [0.0, 1.0]"
                    )
            
            elif param_type == 'utility':
                if base_value < -1.0 or base_value > 1.0:
                    self.warnings.append(
                        f"Parameter '{param_id}' (type: utility) has base_value {base_value} "
                        "outside typical range [-1.0, 1.0]"
                    )
            
            elif param_type == 'cost':
                if base_value < 0:
                    self.warnings.append(
                        f"Parameter '{param_id}' (type: cost) has negative base_value {base_value}"
                    )
            
            elif param_type in ['rate', 'duration']:
                if base_value < 0:
                    self.errors.append(
                        f"Parameter '{param_id}' (type: {param_type}) has negative base_value {base_value}"
                    )
            
            elif param_type == 'relative_risk':
                if base_value <= 0:
                    self.errors.append(
                        f"Parameter '{param_id}' (type: relative_risk) has non-positive base_value {base_value}"
                    )
            
            # Check bounds if specified
            bounds = param.get('bounds', {})
            if bounds:
                lower = bounds.get('lower')
                upper = bounds.get('upper')
                
                if lower is not None and base_value < lower:
                    self.warnings.append(
                        f"Parameter '{param_id}' base_value {base_value} below lower bound {lower}"
                    )
                
                if upper is not None and base_value > upper:
                    self.warnings.append(
                        f"Parameter '{param_id}' base_value {base_value} above upper bound {upper}"
                    )
    
    def print_report(self):
        """Print validation report"""
        is_valid, errors, warnings = self.validate()
        
        print("\n" + "="*70)
        print("HTA SCHEMA VALIDATION REPORT")
        print("="*70)
        
        if self.model:
            metadata = self.model.get('model_metadata', {})
            print(f"\nModel: {metadata.get('model_name', 'Unknown')}")
            print(f"Type: {metadata.get('model_type', 'Unknown')}")
            print(f"Schema Version: {self.model.get('schema_version', 'Unknown')}")
        
        print(f"\nValidation Status: {'✓ PASSED' if is_valid else '✗ FAILED'}")
        print(f"Errors: {len(errors)}")
        print(f"Warnings: {len(warnings)}")
        
        if errors:
            print("\n" + "-"*70)
            print("ERRORS:")
            print("-"*70)
            for i, error in enumerate(errors, 1):
                print(f"{i}. {error}")
        
        if warnings:
            print("\n" + "-"*70)
            print("WARNINGS:")
            print("-"*70)
            for i, warning in enumerate(warnings, 1):
                print(f"{i}. {warning}")
        
        print("\n" + "="*70)
        
        return is_valid


def main():
    """Command line interface"""
    if len(sys.argv) < 2:
        print("Usage: python hta_validator.py <model_file.json> [schema_file.json]")
        print("\nExample:")
        print("  python hta_validator.py example_stroke_thrombolysis.json")
        print("  python hta_validator.py my_model.json hta_schema_v0.1.json")
        sys.exit(1)
    
    model_path = sys.argv[1]
    schema_path = sys.argv[2] if len(sys.argv) > 2 else None
    
    if not Path(model_path).exists():
        print(f"Error: Model file '{model_path}' not found")
        sys.exit(1)
    
    if schema_path and not Path(schema_path).exists():
        print(f"Error: Schema file '{schema_path}' not found")
        sys.exit(1)
    
    try:
        validator = HTASchemaValidator(schema_path, model_path)
        is_valid = validator.print_report()
        sys.exit(0 if is_valid else 1)
    
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in file - {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
