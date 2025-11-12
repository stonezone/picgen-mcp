# 📦 NPM Publishing Guide

## Prerequisites

1. **npm account** - Create one at [npmjs.com](https://www.npmjs.com/signup)
2. **npm CLI installed** - Comes with Node.js
3. **Clean git state** - Commit all changes first

---

## 🚀 Publishing Steps

### Step 1: Login to npm

```bash
npm login
```

Enter your credentials:
- **Username:** Your npm username
- **Password:** Your npm password
- **Email:** Your npm email
- **OTP:** Two-factor auth code (if enabled)

Verify you're logged in:
```bash
npm whoami
# Should display your username
```

### Step 2: Pre-publish Checklist

```bash
# 1. Check current version
cat package.json | grep version

# 2. Test the package locally
npm run test

# 3. Verify package contents
npm pack --dry-run

# 4. Check for common issues
npm doctor
```

### Step 3: Version Bump (Choose One)

```bash
# Patch version (0.2.0 → 0.2.1) - Bug fixes
npm version patch

# Minor version (0.2.0 → 0.3.0) - New features
npm version minor

# Major version (0.2.0 → 1.0.0) - Breaking changes
npm version major
```

This will:
- Update `package.json` version
- Create a git commit
- Create a git tag

### Step 4: Publish to npm

```bash
# Publish to npm registry
npm publish --access public

# Or for scoped packages (recommended)
npm publish
```

**Expected output:**
```
+ @stonezone/imagegen-mcp@0.2.0
```

### Step 5: Push to GitHub

```bash
# Push code and tags
git push
git push --tags
```

### Step 6: Verify Publication

```bash
# Check on npm
npm view @stonezone/imagegen-mcp

# Test installation
npm install -g @stonezone/imagegen-mcp

# Test execution
npx @stonezone/imagegen-mcp --help
```

---

## 🔧 Testing Before Publishing

### Local Testing (Important!)

```bash
# 1. Pack the package
npm pack

# 2. Install the tarball globally
npm install -g stonezone-imagegen-mcp-0.2.0.tgz

# 3. Test the command
imagegen-mcp --help

# 4. Test in Claude Desktop
# Edit ~/.config/claude/mcp_config.json to use:
{
  "imagegen": {
    "command": "imagegen-mcp"
  }
}

# 5. Clean up test installation
npm uninstall -g @stonezone/imagegen-mcp
rm stonezone-imagegen-mcp-0.2.0.tgz
```

### Test in Different Environments

**macOS:**
```bash
# System Python
python3 --version
npx @stonezone/imagegen-mcp

# Homebrew Python
/opt/homebrew/bin/python3 --version
npx @stonezone/imagegen-mcp
```

**Linux:**
```bash
docker run -it --rm node:18 bash
npm install -g @stonezone/imagegen-mcp
imagegen-mcp --help
```

**Windows:**
```powershell
# PowerShell
npx @stonezone/imagegen-mcp
```

---

## 📝 Publishing Checklist

- [ ] All tests pass: `npm test`
- [ ] README.md is up to date
- [ ] CHANGELOG.md updated with new version
- [ ] No uncommitted changes: `git status`
- [ ] Version bumped appropriately
- [ ] Tested locally with `npm pack`
- [ ] Logged into npm: `npm whoami`
- [ ] Published: `npm publish`
- [ ] Pushed to GitHub: `git push && git push --tags`
- [ ] Tested installation: `npm install -g @stonezone/imagegen-mcp`
- [ ] Updated documentation if needed

---

## 🔄 Updating Published Package

### For Bug Fixes (Patch)

```bash
# 1. Fix the bug
# 2. Update tests
# 3. Update CHANGELOG.md
git add .
git commit -m "fix: describe the bug fix"

# 4. Bump patch version
npm version patch

# 5. Publish
npm publish

# 6. Push
git push && git push --tags
```

### For New Features (Minor)

```bash
# 1. Implement feature
# 2. Add tests
# 3. Update README.md and CHANGELOG.md
git add .
git commit -m "feat: describe the new feature"

# 4. Bump minor version
npm version minor

# 5. Publish
npm publish

# 6. Push
git push && git push --tags
```

### For Breaking Changes (Major)

```bash
# 1. Implement breaking changes
# 2. Update all documentation
# 3. Update migration guide in CHANGELOG.md
git add .
git commit -m "feat!: describe breaking change"

# 4. Bump major version
npm version major

# 5. Publish
npm publish

# 6. Push
git push && git push --tags
```

---

## 🐛 Common Publishing Issues

### "You do not have permission to publish"

**Solution:**
```bash
# Check you're logged in
npm whoami

# Login again
npm logout
npm login

# For scoped packages, ensure public access
npm publish --access public
```

### "Version already exists"

**Solution:**
```bash
# Bump the version first
npm version patch
npm publish
```

### "Package name already taken"

**Solution:**
Use a scoped name:
```bash
# In package.json, change:
"name": "imagegen-mcp"
# To:
"name": "@yourusername/imagegen-mcp"
```

### "Invalid package.json"

**Solution:**
```bash
# Validate JSON syntax
cat package.json | python -m json.tool

# Or use online validator
# https://jsonlint.com
```

### Git tag conflicts

**Solution:**
```bash
# Delete local tag
git tag -d v0.2.0

# Delete remote tag
git push origin :refs/tags/v0.2.0

# Recreate tag
npm version patch --force
git push --tags
```

---

## 📊 Post-Publication

### Monitor Your Package

1. **npm package page:**
   ```
   https://www.npmjs.com/package/@stonezone/imagegen-mcp
   ```

2. **Download stats:**
   ```bash
   npm info @stonezone/imagegen-mcp
   ```

3. **Check dependents:**
   ```
   https://www.npmjs.com/browse/depended/@stonezone/imagegen-mcp
   ```

### Promote Your Package

1. **GitHub README badges:**
   ```markdown
   [![npm version](https://img.shields.io/npm/v/@stonezone/imagegen-mcp.svg)](https://www.npmjs.com/package/@stonezone/imagegen-mcp)
   [![npm downloads](https://img.shields.io/npm/dm/@stonezone/imagegen-mcp.svg)](https://www.npmjs.com/package/@stonezone/imagegen-mcp)
   ```

2. **Tag releases on GitHub:**
   - Go to: https://github.com/stonezone/imagegenMCP/releases
   - Click "Create a new release"
   - Select the tag created by `npm version`
   - Add release notes from CHANGELOG.md

3. **Social media:**
   - Tweet about your package
   - Post in relevant Discord/Slack communities
   - Share on Reddit (r/programming, r/node, etc.)

---

## 🔐 Security Best Practices

### Protect Your npm Account

```bash
# Enable 2FA
npm profile enable-2fa auth-and-writes

# Check your profile
npm profile get

# Use tokens for CI/CD
npm token create --read-only
```

### Package Security

```bash
# Audit dependencies
npm audit

# Fix vulnerabilities automatically
npm audit fix

# Check for outdated dependencies
npm outdated

# Update dependencies
npm update
```

---

## 📚 Additional Resources

- [npm Publishing Guide](https://docs.npmjs.com/packages-and-modules/contributing-packages-to-the-registry)
- [Semantic Versioning](https://semver.org/)
- [npm Documentation](https://docs.npmjs.com/)
- [Package.json Reference](https://docs.npmjs.com/cli/v9/configuring-npm/package-json)

---

## 🎯 Quick Reference

### One-Line Publish Flow

```bash
# Patch release
npm test && npm version patch && npm publish && git push --follow-tags

# Minor release
npm test && npm version minor && npm publish && git push --follow-tags

# Major release
npm test && npm version major && npm publish && git push --follow-tags
```

---

**Ready to publish? Let's go! 🚀**
