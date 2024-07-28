# Document Naming Convention

## 1. Introduction
This document outlines the naming convention for all documentation. The purpose is to ensure consistent and clear version control across all project artifacts.

## 2. Naming Convention
2.1 All documents will be named using the following format:
    DocumentName_vX.Y.Z.md
    Where:
    - DocumentName is the descriptive name of the document
    - X.Y.Z is the version number of the document when it was created or last updated
    - .md is the file extension for Markdown files

2.2 Examples:
    - SoftwareDevelopmentPlan_v1.0.0.md
    - SoftwareRequirementsSpecification_v1.0.0.md
    - SoftwareArchitecture_v1.0.0.md

## 3. Version Control
3.1 Git will be used to track all changes to documents, including minor revisions.
3.2 A separate document will track the current version of the project and individual documents.
3.3 The version in a document's filename represents the project version at the time of the document's last update.

## 4. Document Updates
4.1 When updating a document:
    - If the document content is updated, create a new file with the current project version number.
    - The old version of the document should be deleted after creating the new version.

4.2 Version Number Changes:
    - MAJOR (X): Increment when making incompatible changes, such as:
      * Significant restructuring of the project
      * Major changes in project scope or direction
    - MINOR (Y): Increment when adding functionality in a backwards-compatible manner, such as:
      * Adding new features or substantial content
      * Usability improvements that change how users interact with the system
    - PATCH (Z): Increment for backwards-compatible bug fixes or minor updates, such as:
      * Bug fixes
      * Small clarifications that don't change functionality

4.3 Version Tracking Rule:
    - The version of any file must be less than or equal to the current project version.

## 5. Current Version Tracking
5.1 A separate document (e.g., "CurrentVersions.md") will maintain a list of all project documents with their current versions.
5.2 This tracking document will be updated with each version change, ensuring an up-to-date overview of the project's documentation status.

## Version History
- 1.0.0: Initial Document Naming Convention
- 1.1.0: Updated versioning approach, added current version tracking guidelines