# Release Guide

This document describes how to create a new release of py_kit.

## Prerequisites

1. All tests must pass on the main branch
2. All changes should be committed and pushed
3. You should have write access to the repository
4. For PyPI publishing: Configure trusted publishing (see below)

## Release Process

### 1. Update Version

Edit the version in the following files:
- `src/py_kit/__init__.py` - Update `__version__`
- `pyproject.toml` - Update `version`

```python
# src/py_kit/__init__.py
__version__ = "0.2.0"
```

```toml
# pyproject.toml
[project]
version = "0.2.0"
```

### 2. Update Changelog

Create or update `CHANGELOG.md` with the new version's changes:

```markdown
## [0.2.0] - 2025-10-22

### Added
- Rich logging module with file and console output
- Enhanced terminal output with rich formatting
- Automatic GitHub Release creation on tag push
- Automatic PyPI publishing on tag push

### Changed
- Updated main.py to use rich formatting

### Fixed
- (list any bug fixes)
```

### 3. Commit Changes

```bash
git add .
git commit -m "chore: bump version to 0.2.0"
git push origin main
```

### 4. Create and Push Tag

```bash
# Create an annotated tag
git tag -a v0.2.0 -m "Release version 0.2.0"

# Push the tag to GitHub
git push origin v0.2.0
```

### 5. Automated Process

Once the tag is pushed, the following happens automatically:

1. **GitHub Actions: Release**
   - Runs tests to verify the release
   - Builds distribution packages (wheel and sdist)
   - Generates changelog from git commits
   - Creates a GitHub Release with release notes
   - Attaches distribution files to the release

2. **GitHub Actions: Publish to PyPI**
   - Validates the release (tests, linting)
   - Verifies version matches tag
   - Builds distribution packages
   - Publishes to TestPyPI (for testing)
   - Publishes to PyPI (production)

## PyPI Publishing Setup

### Option 1: Trusted Publishing (Recommended)

Trusted publishing eliminates the need for API tokens:

1. Go to [PyPI Trusted Publishers](https://pypi.org/manage/account/publishing/)
2. Add a new publisher:
   - PyPI Project Name: `py-ref`
   - Owner: `gqy22`
   - Repository: `py_kit`
   - Workflow name: `publish.yml`
   - Environment name: `pypi`

3. Repeat for TestPyPI at [TestPyPI Trusted Publishers](https://test.pypi.org/manage/account/publishing/)

### Option 2: API Tokens (Alternative)

If you prefer using API tokens:

1. Generate API token at [PyPI API tokens](https://pypi.org/manage/account/token/)
2. Add to GitHub secrets:
   - Go to repository Settings → Secrets and variables → Actions
   - Add secret: `PYPI_API_TOKEN`
3. Update `.github/workflows/publish.yml` to use token authentication

## Manual Release (Fallback)

If automated release fails, you can publish manually:

### Build Distribution

```bash
# Ensure build tools are installed
uv pip install build twine

# Build packages
python -m build

# Verify packages
twine check dist/*
```

### Publish to TestPyPI

```bash
# Upload to TestPyPI first
twine upload --repository testpypi dist/*

# Test installation
pip install --index-url https://test.pypi.org/simple/ py-ref
```

### Publish to PyPI

```bash
# Upload to PyPI
twine upload dist/*

# Verify installation
pip install py-ref
```

## Version Numbering

We follow [Semantic Versioning](https://semver.org/):

- **MAJOR.MINOR.PATCH** (e.g., 1.2.3)
  - **MAJOR**: Breaking changes
  - **MINOR**: New features (backward compatible)
  - **PATCH**: Bug fixes (backward compatible)

Examples:
- `v0.1.0` → `v0.1.1`: Bug fixes
- `v0.1.1` → `v0.2.0`: New features
- `v0.2.0` → `v1.0.0`: Breaking changes or stable release

## Hotfix Releases

For urgent bug fixes:

1. Create a hotfix branch from the tag:
   ```bash
   git checkout -b hotfix/0.2.1 v0.2.0
   ```

2. Make the fix and commit:
   ```bash
   git commit -m "fix: critical bug in logger"
   ```

3. Update version to 0.2.1 and create tag:
   ```bash
   git tag -a v0.2.1 -m "Hotfix release 0.2.1"
   git push origin v0.2.1
   ```

4. Merge back to main:
   ```bash
   git checkout main
   git merge hotfix/0.2.1
   git push origin main
   ```

## Rollback

If a release has issues:

1. **Delete the tag** (if not published to PyPI yet):
   ```bash
   git tag -d v0.2.0
   git push origin :refs/tags/v0.2.0
   ```

2. **Yank the release from PyPI** (if already published):
   - Go to PyPI project page
   - Find the version and click "Options" → "Yank"
   - Or use: `twine yank py-ref 0.2.0`

3. **Fix issues and release a new version** (e.g., 0.2.1)

## Troubleshooting

### Tag already exists
```bash
# Delete local tag
git tag -d v0.2.0

# Delete remote tag
git push origin :refs/tags/v0.2.0

# Create new tag
git tag -a v0.2.0 -m "Release version 0.2.0"
git push origin v0.2.0
```

### Version mismatch error
Ensure version in `pyproject.toml` and `__init__.py` match the tag (without 'v' prefix).

### Build fails
```bash
# Clean build artifacts
rm -rf build/ dist/ *.egg-info

# Rebuild
python -m build
```

### PyPI upload fails
- Check you have permissions on PyPI project
- Verify trusted publishing is configured
- Ensure version doesn't already exist on PyPI

## Checklist

Before creating a release:

- [ ] All tests pass locally
- [ ] All tests pass in CI
- [ ] Version updated in `__init__.py`
- [ ] Version updated in `pyproject.toml`
- [ ] CHANGELOG.md updated
- [ ] Changes committed and pushed
- [ ] Tag created with correct version
- [ ] Tag pushed to GitHub
- [ ] Release created on GitHub (automatic)
- [ ] Package published to PyPI (automatic)
- [ ] Installation verified: `pip install py-ref==X.Y.Z`

## Post-Release

After a successful release:

1. Announce the release (optional):
   - GitHub Discussions
   - Social media
   - Project documentation

2. Monitor for issues:
   - Check GitHub Issues
   - Monitor PyPI download stats

3. Start planning next release:
   - Create milestone for next version
   - Label issues and PRs accordingly
