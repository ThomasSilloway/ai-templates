# /// script
# dependencies = [
#   "rich>=13.0.0",
#   "pathlib>=1.0.1"
# ]
# ///

"""File generation for template files."""

import logging
from pathlib import Path
from typing import Dict
from rich.console import Console

console = Console()
logger = logging.getLogger(__name__)

class FileGenerator:
    """Handles template file generation."""
    
    def __init__(self, templates_path: str = "ai-specs/templates"):
        self.templates_path = Path(templates_path)
        
    def generate_files(
        self, 
        target_path: Path,
        template_files: list[str],
        variables: Dict[str, str]
    ) -> None:
        """Generate files from templates with variable replacement."""
        # Handle feature_overview.md separately
        self._generate_feature_overview(target_path, variables)
        
        # Process remaining template files
        for template_file in template_files:
            self._process_template_file(target_path, template_file, variables)
    
    def _generate_feature_overview(self, target_path: Path, variables: Dict[str, str]) -> None:
        """Generate feature_overview.md from user input."""
        target_file = target_path / "feature_overview.md"
        try:
            target_file.write_text(variables["feature_overview"], encoding='utf-8')
            console.print(f"Generated file: [green]{target_file.relative_to(target_path)}[/]")
        except Exception as e:
            logger.error(f"Failed to generate feature_overview.md: {e}")
            raise

    def _process_template_file(
        self,
        target_path: Path,
        template_file: str,
        variables: Dict[str, str]
    ) -> None:
        """Process a single template file."""
        source_path = self.templates_path / template_file
        target_file = target_path / template_file
        
        try:
            if not source_path.exists():
                logger.error(f"Template file not found: {source_path}")
                raise FileNotFoundError(f"Template file not found: {source_path}")
            
            content = source_path.read_text(encoding='utf-8')
            for var_name, var_value in variables.items():
                placeholder = "{{" + f" {var_name} " + "}}"
                content = content.replace(placeholder, var_value)
            
            target_file.write_text(content, encoding='utf-8')
            console.print(f"Generated file: [green]{target_file.relative_to(target_path)}[/]")
        except Exception as e:
            logger.error(f"Error processing {template_file}: {e}")
            raise