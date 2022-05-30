import sys
lib_dynload="__LIBDIR__/lib-dynload"
site_packages="__LIBDIR__/site-packages"
for i in range(len(sys.path)):
    if sys.path[i] in [lib_dynload, site_packages]:
        sys.path.insert(i, f"{site_packages}/readline")
        break
