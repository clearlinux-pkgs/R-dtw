#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-dtw
Version  : 1.21.3
Release  : 52
URL      : https://cran.r-project.org/src/contrib/dtw_1.21-3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/dtw_1.21-3.tar.gz
Summary  : Dynamic Time Warping Algorithms
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-dtw-lib = %{version}-%{release}
Requires: R-proxy
BuildRequires : R-Rcpp
BuildRequires : R-analogue
BuildRequires : R-fossil
BuildRequires : R-proxy
BuildRequires : buildreq-R
BuildRequires : util-linux

%description
No detailed description available

%package lib
Summary: lib components for the R-dtw package.
Group: Libraries

%description lib
lib components for the R-dtw package.


%prep
%setup -q -c -n dtw

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1571821121

%install
export SOURCE_DATE_EPOCH=1571821121
rm -rf %{buildroot}
export LANG=C.UTF-8
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library dtw
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library dtw
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library dtw
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc dtw || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/dtw/CITATION
/usr/lib64/R/library/dtw/ChangeLog
/usr/lib64/R/library/dtw/DESCRIPTION
/usr/lib64/R/library/dtw/INDEX
/usr/lib64/R/library/dtw/Meta/Rd.rds
/usr/lib64/R/library/dtw/Meta/data.rds
/usr/lib64/R/library/dtw/Meta/demo.rds
/usr/lib64/R/library/dtw/Meta/features.rds
/usr/lib64/R/library/dtw/Meta/hsearch.rds
/usr/lib64/R/library/dtw/Meta/links.rds
/usr/lib64/R/library/dtw/Meta/nsInfo.rds
/usr/lib64/R/library/dtw/Meta/package.rds
/usr/lib64/R/library/dtw/Meta/vignette.rds
/usr/lib64/R/library/dtw/NAMESPACE
/usr/lib64/R/library/dtw/R/dtw
/usr/lib64/R/library/dtw/R/dtw.rdb
/usr/lib64/R/library/dtw/R/dtw.rdx
/usr/lib64/R/library/dtw/data/aami3a.rda
/usr/lib64/R/library/dtw/data/aami3b.rda
/usr/lib64/R/library/dtw/demo/dtw.R
/usr/lib64/R/library/dtw/doc/dtw.R
/usr/lib64/R/library/dtw/doc/dtw.Rnw
/usr/lib64/R/library/dtw/doc/dtw.pdf
/usr/lib64/R/library/dtw/doc/index.html
/usr/lib64/R/library/dtw/dtw.bib
/usr/lib64/R/library/dtw/help/AnIndex
/usr/lib64/R/library/dtw/help/aliases.rds
/usr/lib64/R/library/dtw/help/dtw.rdb
/usr/lib64/R/library/dtw/help/dtw.rdx
/usr/lib64/R/library/dtw/help/paths.rds
/usr/lib64/R/library/dtw/html/00Index.html
/usr/lib64/R/library/dtw/html/R.css
/usr/lib64/R/library/dtw/tests/dtw_test.R
/usr/lib64/R/library/dtw/tests/dtw_test.Rout.save

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/dtw/libs/dtw.so
/usr/lib64/R/library/dtw/libs/dtw.so.avx2
