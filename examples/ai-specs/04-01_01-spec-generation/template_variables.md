# Template Variable System Documentation

## Core Variables

### Common Variables (Used across all templates)
```
{{ feature_name }}         # Short descriptive name of the feature
{{ feature_overview }}     # Complete feature overview text
{{ project_details }}      # Content from project-summary.md
{{ generated_folder }}     # Full path to the generated folder for this feature
{{ current_date }}        # Current date in MM-DD format
{{ feature_number }}      # Sequential number for multiple features on same date
```

## Template-Specific Variables

### feature_overview.md
```
No additional variables - uses core variables only
```

### spec-architecture-brainstorm-and-prd.md
```
{{ relevant_files }}      # List of relevant files (optional, can be empty)
```

### spec-document-progress.md
```
{{ docs_list }}          # List of related documentation (optional, can be empty)
```

### spec_bug_fixing_all.md
```
{{ bug_description }}    # <USER INPUT REQUIRED> placeholder until bug occurs
{{ prd_link }}          # Link to the PRD document
{{ change_notes }}      # Link to change notes document
```

### spec_polish.md and spec_polish_small.md
```
{{ polish_items }}      # <USER INPUT REQUIRED> placeholder until polish needed
{{ related_files }}     # List of related files
{{ prd_link }}         # Link to the PRD document
{{ change_notes }}     # Link to change notes document
```

## Suggested Template Updates

1. **Standardize Placeholder Format**
   - Change all `<INSERT>` to use Jinja2 syntax: `{{ variable_name }}`
   - Update all references to use consistent variable names

2. **Path References**
   - Add `{{ base_path }}` variable for consistent path references
   - Use path joining in templates instead of hardcoded slashes

3. **Documentation Links**
   - Standardize format: `@{{ base_path }}/path/to/document.md`
   - Add support for automatic link validation

4. **Generated Folder References**
   - Replace "using the Generated Folder Path above" text with direct variable usage
   - Add helper for relative path generation

## Template Variable Usage Examples

### Example 1: Basic Template
```markdown
# {{ feature_name }}

{{ feature_overview }}

## Project Context
{{ project_details }}
```

### Example 2: Path Generation
```markdown
## Generated Content
Content will be created in: {{ generated_folder }}/generated/
Bug reports will be stored in: {{ generated_folder }}/generated/bugs/
```

### Example 3: Date-Based Content
```markdown
# Feature Implementation Log
Started on: {{ current_date }}
Feature Number: {{ feature_number }}
```

## Implementation Notes

1. **Variable Collection**
   - Collect feature_name and feature_overview through interactive prompts
   - Auto-generate date and feature number
   - Load project_details from project-summary.md
   - Generate folder paths based on naming convention

2. **Variable Validation**
   - Ensure required variables are present
   - Validate path-based variables
   - Check for valid content in loaded files

3. **Template Processing**
   - Use Jinja2 for template rendering
   - Support conditional sections based on variable presence
   - Handle optional variables gracefully

4. **File Generation**
   - Create all necessary directories
   - Process templates in correct order
   - Maintain file relationships