# Overview

  Some work on this new feature has already begun, let's document the progress thus far into /ai-docs/changelog/<number>-app-updates.md

  Follow each task below one by one, make sure not to skip any steps.

  For all .md file changes use Architect mode

  For all code changes use Code mode

## Feature Overview

{{ feature_overview }}


## Docs

PRD: @/{{ prd_link }}

Change Notes: @/{{ change_notes }}

## Project Details

{{ project_details }} 

## IMPORTANT
 - DO NOT EDIT ANY CODE 

## Tasks

### Add changelog file
```
- FIND the last change log number in /ai-docs/changelog/
- CREATE /ai-docs/changelog/<next-number>-app-updates-<3 word description>.md
- ANALYZE the current project
- UPDATE app updates file with the latest updates we have implemented thus far in the PRD
```

### Update project summary
```
 - READ @/project-summary.md
   - Purpose: to help summarize the project to an LLM agent
 - CONSIDER changes from the latest feature that may need to be included
 - UPDATE project-summary.md by seamlessly integrating the existing summary with any of these new details into a nice summary for future LLMs to use as a reference for the entire project
```

### Update tech design doc
```
- ANALYZE @/project-tech-design.md and see if any changes are necessary due to the new changes.
  - The purpose of this file is to help a coding architect LLM understand what files to change when it comes to bug fixing or making a new feature
- UPDATE the tech design doc with any changes
```
