# Deployment Guide

This guide explains how to deploy your portfolio to GitHub Pages using the automated workflow.

## Prerequisites

- GitHub repository: `thundergore/super-giggle`
- GitHub Pages enabled on your repository

## Setup Steps

### 1. Enable GitHub Pages

1. Go to your repository on GitHub: https://github.com/thundergore/super-giggle
2. Click **Settings** → **Pages** (in the left sidebar)
3. Under **Source**, select:
   - **Deploy from a branch**
   - Branch: `gh-pages` (this will be created automatically by the workflow)
   - Folder: `/ (root)`
4. Click **Save**

### 2. Push Your Changes

```bash
# Check current status
git status

# Add all new files
git add .

# Commit changes
git commit -m "Refactor portfolio to v2.0 with interactive Plotly visualizations

- Convert from Jupyter notebook to modular Python codebase
- Replace static matplotlib charts with interactive Plotly visualizations
- Add comprehensive test suite (29 tests)
- Implement Tailwind CSS responsive design
- Add methodology documentation
- Remove specific achievement metrics (use year-based dates only)
- Set up GitHub Actions for automated deployment

🤖 Generated with Claude Code"

# Push to main branch
git push origin main
```

### 3. Monitor Deployment

1. Go to the **Actions** tab in your GitHub repository
2. Watch the "Generate and Deploy Portfolio" workflow run
3. It will:
   - ✓ Install dependencies
   - ✓ Run tests (all 29 tests must pass)
   - ✓ Generate visualizations
   - ✓ Deploy to `gh-pages` branch

### 4. Access Your Site

Once the workflow completes (usually 1-2 minutes):

- Your portfolio will be live at: **https://thundergore.github.io/super-giggle/**
- GitHub Pages automatically serves from the `gh-pages` branch
- Updates deploy automatically on every push to `main`

## Manual Deployment (Optional)

You can also trigger deployment manually:

1. Go to **Actions** tab
2. Click **Generate and Deploy Portfolio**
3. Click **Run workflow** → **Run workflow**

## Troubleshooting

### Workflow Fails

**Check the Actions tab for error details:**

```bash
# Common issues:

# 1. Tests failing
# Run locally first:
pytest tests/

# 2. Missing dependencies
# Verify requirements.txt has all packages

# 3. Python version mismatch
# Workflow uses Python 3.11
```

### GitHub Pages Not Updating

1. Check **Actions** tab - ensure workflow completed successfully
2. Check **Settings** → **Pages** - verify `gh-pages` branch is selected
3. GitHub Pages can take 1-2 minutes to update after deployment
4. Clear browser cache (Cmd+Shift+R / Ctrl+Shift+F5)

### Visualizations Not Loading

If you see the HTML but charts don't display:

1. Check browser console for errors (F12 → Console)
2. Verify all visualization files are in `output/visualizations/`
3. Check file paths in `output/index.html` (should be relative: `visualizations/*.html`)

## Local Testing Before Deploy

Always test locally before pushing:

```bash
# 1. Run tests
pytest tests/

# 2. Generate visualizations
python src/generate.py

# 3. View locally
python -m http.server 8000 --directory output
# Visit: http://localhost:8000

# 4. If everything looks good, commit and push
git add .
git commit -m "Update portfolio data"
git push origin main
```

## Updating Your Portfolio

To update your portfolio in the future:

1. **Update data** in `src/data/*.py`
2. **Run tests** to validate: `pytest tests/`
3. **Generate locally** to preview: `python src/generate.py`
4. **Commit and push** to main branch
5. **GitHub Actions automatically deploys** the updates

## Custom Domain (Optional)

To use a custom domain like `portfolio.yourdomain.com`:

1. Add a CNAME record in your DNS settings pointing to: `thundergore.github.io`
2. In `deploy.yml`, change:
   ```yaml
   cname: false
   ```
   to:
   ```yaml
   cname: portfolio.yourdomain.com
   ```
3. In GitHub **Settings** → **Pages**, add your custom domain
4. Commit and push the workflow change

## Monitoring

### View Deployment History

- **Actions** tab shows all deployment runs with timestamps
- Each run shows which commit triggered it
- Click any run to see detailed logs

### Check Site Status

```bash
# Visit your site
open https://thundergore.github.io/super-giggle/

# Check when it was last updated
# (Look at "Last Updated" date in the footer or methodology section)
```

## Next Steps After First Deploy

1. ✓ Verify your site is live
2. Update LinkedIn profile with portfolio link
3. Share the link on social media
4. Monitor GitHub Actions for successful deployments
5. Update portfolio data as your skills grow

## Need Help?

- **GitHub Actions docs**: https://docs.github.com/en/actions
- **GitHub Pages docs**: https://docs.github.com/en/pages
- **Repository**: https://github.com/thundergore/super-giggle
