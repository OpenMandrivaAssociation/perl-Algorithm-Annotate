%define upstream_name	 Algorithm-Annotate
%define upstream_version 0.10

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:	Perl module to represent a series of changes in annotate form
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:    ftp://ftp.perl.org/pub/CPAN/modules/by-module/Algorithm/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:  perl(Algorithm::Diff)
BuildArch:      noarch
BuildRoot:	    %{_tmppath}/%{name}-%{version}-%{release}

%description
Algorithm::Annotate generates a list that is useful for generating output
similar to cvs annotate

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
