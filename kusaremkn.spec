Summary: Great Genius Pretty Girl Programming Beginner
Summary(ja): 大天才美少女プログラミング初心者
Name: KusaReMKN
Version: 1.0.0
Release: git_%{_commit_id}%{?dist}
License: MIT
URL: https://github.com/KusaReMKN/KusaReMKN.1
Group: Development/Tools/Other
Vendor: KusaReMKN
Packager: IchikawaYukko
BuildArch: x86_64
Source: %{name}-%{version}-%{release}.src.tar.gz
Prefix: /usr


%description
KusaReMKN is a corrupt mikan that calls herself “great genius pretty girl programming beginner”.
You can call her Mikan-chan!  She is a seriously KAWAII girl, plus she has a cock, which is a great deal.


%description -l ja
KusaReMKN（腐れ蜜柑） 私は大天才美少女プログラミング初心者
立派な女の子です。しかもちんちんがついてお得！


# 更新履歴
%changelog
* Sun May 4 2025 IchikawaYukko
- First RPM package release


%prep
###  Binaries ###
#echo "BUILDROOT = "%{buildroot}
mkdir -p %{buildroot}/usr/bin/
mkdir -p %{buildroot}/usr/share/man/man1
#mkdir -p %{buildroot}/usr/share/man/ja/man1

#echo "SRC_ROOT = $SRC_ROOT"
cp $SRC_ROOT/KusaReMKN %{buildroot}/usr/bin
gzip -9 -c $SRC_ROOT/kusaremkn.1 > %{buildroot}/usr/share/man/man1/KusaReMKN.1.gz
#gzip -9 -c $SRC_ROOT/kusaremkn.1.ja > %{buildroot}/usr/share/man/ja/man1/KusaReMKN.1.gz

### Sources ###
cp $SRC_ROOT/kusaremkn.c %{_sourcedir}/kusaremkn.c
tar cfz %{_sourcedir}/%{name}-%{version}-%{release}.src.tar.gz -C %{_sourcedir} kusaremkn.c
exit


%files
%attr(0755, root, root) /usr/bin/*
%attr(0664, root, root) /usr/share/man/man1/*
#%attr(0664, root, root) /usr/share/man/ja/man1/*


%clean
rm -rf %{buildroot}/usr
ls -lZ %{_srcrpmdir}/* %{_rpmdir}/x86_64/*

