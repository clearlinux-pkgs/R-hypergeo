#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-hypergeo
Version  : 1.2.13
Release  : 12
URL      : https://cran.r-project.org/src/contrib/hypergeo_1.2-13.tar.gz
Source0  : https://cran.r-project.org/src/contrib/hypergeo_1.2-13.tar.gz
Summary  : The Gauss Hypergeometric Function
Group    : Development/Tools
License  : GPL-2.0
BuildRequires : R-contfrac
BuildRequires : R-deSolve
BuildRequires : R-elliptic
BuildRequires : buildreq-R

%description
No detailed description available

%prep
%setup -q -c -n hypergeo

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552893435

%install
export SOURCE_DATE_EPOCH=1552893435
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library hypergeo
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library hypergeo
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library hypergeo
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  hypergeo || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/hypergeo/DESCRIPTION
/usr/lib64/R/library/hypergeo/INDEX
/usr/lib64/R/library/hypergeo/Meta/Rd.rds
/usr/lib64/R/library/hypergeo/Meta/features.rds
/usr/lib64/R/library/hypergeo/Meta/hsearch.rds
/usr/lib64/R/library/hypergeo/Meta/links.rds
/usr/lib64/R/library/hypergeo/Meta/nsInfo.rds
/usr/lib64/R/library/hypergeo/Meta/package.rds
/usr/lib64/R/library/hypergeo/Meta/vignette.rds
/usr/lib64/R/library/hypergeo/NAMESPACE
/usr/lib64/R/library/hypergeo/R/hypergeo
/usr/lib64/R/library/hypergeo/R/hypergeo.rdb
/usr/lib64/R/library/hypergeo/R/hypergeo.rdx
/usr/lib64/R/library/hypergeo/doc/hypergeometric.R
/usr/lib64/R/library/hypergeo/doc/hypergeometric.Rnw
/usr/lib64/R/library/hypergeo/doc/hypergeometric.pdf
/usr/lib64/R/library/hypergeo/doc/index.html
/usr/lib64/R/library/hypergeo/help/AnIndex
/usr/lib64/R/library/hypergeo/help/aliases.rds
/usr/lib64/R/library/hypergeo/help/hypergeo.rdb
/usr/lib64/R/library/hypergeo/help/hypergeo.rdx
/usr/lib64/R/library/hypergeo/help/paths.rds
/usr/lib64/R/library/hypergeo/html/00Index.html
/usr/lib64/R/library/hypergeo/html/R.css
/usr/lib64/R/library/hypergeo/tests/aaa.R
/usr/lib64/R/library/hypergeo/tests/aab.R
