#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-dtw
Version  : 1.23.1
Release  : 79
URL      : https://cran.r-project.org/src/contrib/dtw_1.23-1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/dtw_1.23-1.tar.gz
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

%description
(DTW) algorithms in R.  DTW computes the optimal (least cumulative
    distance) alignment between points of two time series.  Common DTW
    variants covered include local (slope) and global (window)
    constraints, subsequence matches, arbitrary distance definitions,
    normalizations, minimum variance matching, and so on.  Provides
    cumulative distances, alignments, specialized plot styles, etc.,

%package lib
Summary: lib components for the R-dtw package.
Group: Libraries

%description lib
lib components for the R-dtw package.


%prep
%setup -q -n dtw
cd %{_builddir}/dtw

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1663691428

%install
export SOURCE_DATE_EPOCH=1663691428
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


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
/usr/lib64/R/library/dtw/tests/Rplots.pdf
/usr/lib64/R/library/dtw/tests/dtw_test.R
/usr/lib64/R/library/dtw/tests/dtw_test.Rout.save

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/dtw/libs/dtw.so
/usr/lib64/R/library/dtw/libs/dtw.so.avx2
/usr/lib64/R/library/dtw/libs/dtw.so.avx512
