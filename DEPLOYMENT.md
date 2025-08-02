# Deployment Instructions for The Last Light

This document provides complete instructions for deploying "The Last Light" book to GitHub Pages.

## Current Deployment Status

The project is already configured with GitHub Actions workflows for deployment:

1. **Build Workflow** (`.github/workflows/build.yml`) - Builds and deploys the book to GitHub Pages
2. **Lint Workflow** (`.github/workflows/lint.yml`) - Runs quality checks on the content
3. **Test Workflow** (`.github/workflows/test.yml`) - Runs tests on the book content

## Prerequisites

Before deploying, ensure you have:

1. A GitHub account
2. A fork or copy of this repository
3. GitHub Pages enabled for your repository

## Deployment Process

### Option 1: Automatic Deployment with GitHub Actions (Recommended)

The project is already configured with GitHub Actions for automatic deployment:

1. **Push to Main Branch**: Any push to the `main` branch will automatically trigger:
   - Build process that combines all chapters
   - Deployment to GitHub Pages

2. **View Your Site**: After the workflow completes, your site will be available at:
   `https://[your-username].github.io/the-last-light/`

### Option 2: Manual Deployment

If you prefer to deploy manually:

1. **Build the Combined Book**:
   ```bash
   chmod +x f.Scripts/combine-book.sh
   ./f.Scripts/combine-book.sh
   ```

2. **Commit All Changes**:
   ```bash
   git add .
   git commit -m "Deploy updated book content"
   git push origin main
   ```

## GitHub Pages Configuration

To configure GitHub Pages for your repository:

1. Go to your repository settings on GitHub
2. Scroll down to the "Pages" section
3. Under "Source", select "GitHub Actions"
4. Save the settings

## Required Files for GitHub Pages

The following files are already included and configured for GitHub Pages:

- `index.html` - Main entry point for the Docsify site
- `_sidebar.md` - Navigation structure for the book
- `404.html` - Custom 404 page for broken links
- `.nojekyll` - Disables Jekyll processing on GitHub Pages
- All Markdown content files in organized directories

## Custom Domain (Optional)

To use a custom domain:

1. Add a `CNAME` file to the root of your repository with your domain name:
   ```
   your-domain.com
   ```

2. Configure your DNS provider to point your domain to GitHub Pages

## Troubleshooting

### Common Issues

1. **Site Not Updating**: 
   - Check that the GitHub Actions workflow completed successfully
   - Verify you're pushing to the `main` branch
   - Allow 1-10 minutes for changes to appear

2. **Broken Links**:
   - The site uses relative paths for all internal links
   - If you see broken links, check the `_sidebar.md` file structure

3. **CSS Not Loading**:
   - The site uses CDN-hosted Docsify themes
   - Ensure you have internet connectivity to load CSS/JS assets

### Checking Deployment Status

You can check the status of your deployment:

1. Go to your repository on GitHub
2. Click on the "Actions" tab
3. View the status of recent workflows

## Updating Content

To update the book content:

1. Edit the Markdown files in their respective directories
2. Commit and push to the `main` branch
3. The GitHub Actions workflow will automatically deploy the changes

## Monitoring

The project includes several quality checks that run automatically:

- Markdown linting for consistent formatting
- Spell checking for content quality
- Link validation to catch broken references

These checks help ensure content quality and consistency across updates.