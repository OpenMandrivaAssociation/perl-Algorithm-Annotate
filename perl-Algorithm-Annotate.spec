
%define realname	Algorithm-Annotate

Name:		perl-%{realname}
Version:	0.10
Release: %mkrel 9
License:	GPL or Artistic
Group:		Development/Perl
Summary:	Perl module to represent a series of changes in annotate form
Source0:        ftp://ftp.perl.org/pub/CPAN/modules/by-module/Algorithm/%{realname}-%{version}.tar.gz
Url:		http://search.cpan.org/dist/%{realname}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	perl-devel
BuildRequires:  perl(Algorithm::Diff)
BuildArch:      noarch
%description
Algorithm::Annotate generates a list that is useful for generating output
similar to cvs annotate

%prep
%setup -q -n %{realname}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)

%{perl_vendorlib}/*
%{_mandir}/man3/*


