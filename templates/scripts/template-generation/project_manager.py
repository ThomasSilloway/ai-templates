# /// script
# dependencies = [
#   "rich>=13.0.0"
# ]
# ///

"""Project details management for template generation.

This module handles loading and parsing project details from project-summary.md.
"""

from pathlib import Path
from typing import Optional
from rich.console import Console

console = Console()

class ProjectManager:
    """Handles loading and managing project details."""
    
    def __init__(self, project_summary_path: Path, project_tech_design_path: Path):
        self.project_summary_path = project_summary_path
        self.project_tech_design_path = project_tech_design_path
        self._project_details: Optional[str] = None
        self._project_tech_design: Optional[str] = None
        
    def load_project_details(self) -> str:
        """Load project details from project-summary.md.
        
        Returns:
            str: Project details content
            
        Raises:
            FileNotFoundError: If project summary file not found
        """
        try:
            if not self._project_details:
                if not self.project_summary_path.exists():
                    raise FileNotFoundError(
                        f"Project summary file not found: {self.project_summary_path}"
                    )
                
                self._project_details = self.project_summary_path.read_text(encoding='utf-8')
                console.print(f"Loaded project details from: [green]{self.project_summary_path}[/]")
                
            return self._project_details
            
        except FileNotFoundError:
            raise

    def _load_project_tech_design(self) -> str:
        """Load project tech design from the configured path.

        Returns:
            str: Project tech design content

        Raises:
            FileNotFoundError: If project tech design file not found
        """
        try:
            if not self._project_tech_design:
                if not self.project_tech_design_path.exists():
                    raise FileNotFoundError(
                        f"Project tech design file not found: {self.project_tech_design_path}"
                    )
                
                self._project_tech_design = self.project_tech_design_path.read_text(encoding='utf-8')
                console.print(f"Loaded project tech design from: [green]{self.project_tech_design_path}[/]")
                
            return self._project_tech_design
            
        except FileNotFoundError:
            raise
        except Exception as e:
            console.print(f"[bold red]Error:[/] Failed to load project tech design: {e}")
            raise
        except Exception as e:
            console.print(f"[bold red]Error:[/] Failed to load project details: {e}")
            raise

    def get_template_variables(self, feature_name: str, feature_overview: str, folder_path: Path) -> dict:
        """Get dictionary of template variables.
        
        Args:
            feature_name: Name of the feature
            feature_overview: Feature overview content
            folder_path: Path to generated feature folder
            
        Returns:
            dict: Template variables
        """
        project_details = self.load_project_details()
        project_tech_design = self._load_project_tech_design()
        
        return {
            "feature_name": feature_name,
            "feature_overview": feature_overview,
            "project_details": project_details,
            "project_tech_design": project_tech_design,
            "generated_folder": str(folder_path),
            "prd_link": str(folder_path / "generated/prd.md"),
            "change_notes": str(folder_path / "generated/change_notes.md")
        }