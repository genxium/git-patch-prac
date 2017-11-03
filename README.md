This repository is created for internal training only.

There're 2 branches prepared for practice, where branch `fix` is 2 commits ahead and to be merged into `master` by the following different approaches.
  - merging
    - [git-merge](https://git-scm.com/docs/git-merge) 
  - patching
    - creating by [git-format-patch](https://git-scm.com/docs/git-format-patch)
    - applying dry-run by [git-apply](https://git-scm.com/docs/git-apply)
    - applying by [git-am](https://git-scm.com/docs/git-am)

The `merging` approach is ordinary.

Recommended steps for practicing the `patching` approach are as follows.
```
# Switch the branch `fix`.
shell> git checkout fix

# Create a collection of "*.patch" files from branch `fix` w.r.t. the "topmost local commit" of branch `master` as a reference for diff, i.e. as the <since> parameter.
shell> git format-patch master

# Save the created "*.patch" files somewhere.

# Switch back to branch `master`, or just clone it into another computer.
shell> git checkout master

# Apply dry-run checking of the patch.
shell> git apply [--stat | --check] /path/to/<any>.patch

# Apply the collection of "*.patch" files in order. 
# Note that if you have several ordered commits and corresponding "*.patch" files created w.r.t. the same reference commit, i.e. the same <since> parameter, then each "*.patch" file contains only the diff information w.r.t. the "*.patch" file of its previous commit. 
shell> git am /path/to/<each_in_order>.patch
```
