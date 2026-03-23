## remote-app

## Create new release

1. commit changes

```bash
git add .
git commit -m "Update version"
git push origin
```

2. Update version in version file

This will emulate ci/cd generating the version file

3. Update version in app.py



4. Create tag

```bash
VER=1.0.0; git tag ${VER} -a -m "Release version ${VER}"; git push origin ${VER}
```

## Delete tag

```bash
VER=1.0.0; git tag -d ${VER} ; git push origin --delete ${VER};
```