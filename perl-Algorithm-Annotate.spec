%define upstream_name	 Algorithm-Annotate
%define upstream_version 0.10

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Perl module to represent a series of changes in annotate form
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:    ftp://ftp.perl.org/pub/CPAN/modules/by-module/Algorithm/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:  perl-devel
BuildRequires:  perl(Algorithm::Diff)
BuildArch:      noarch

%description
Algorithm::Annotate generates a list that is useful for generating output
similar to cvs annotate

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%{perl_vendorlib}/*
%{_mandir}/man3/*


%changelog
* Sat Apr 16 2011 Funda Wang <fwang@mandriva.org> 0.100.0-2mdv2011.0
+ Revision: 653384
- rebuild for updated spec-helper

* Sat Aug 01 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.100.0-1mdv2011.0
+ Revision: 405953
- rebuild using %%perl_convert_version

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.10-9mdv2009.0
+ Revision: 255260
- rebuild

* Sat Dec 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.10-7mdv2008.1
+ Revision: 136882
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Oct 27 2006 Nicolas LÃ©cureuil <neoclust@mandriva.org> 0.10-6mdv2007.0
+ Revision: 73173
- import perl-Algorithm-Annotate-0.10-6mdv2007.0

* Fri Jul 21 2006 Michael Scherer <misc@mandriva.org> 0.10-6mdv2007.0
- Rebuild

* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.10-5mdk
- Fix BuildRequires Using perl Policies
	- Source URL
	- BuildRequires
- use mkrel

* Fri Apr 29 2005 Michael Scherer <misc@mandriva.org> 0.10-4mdk
- use check macro ( and also for amd64 )

* Sat Feb 05 2005 Sylvie Terjan <erinmargault@mandrake.org> 0.10-3mdk
- rebuild for new Perl

* Wed Sep 01 2004 Michael Scherer <misc@mandrake.org> 0.10-2mdk 
- rebuild for new perl ( [DIRM] )

* Sat Apr 03 2004 Michael Scherer <misc@mandrake.org> 0.10-1mdk 
- First MandrakeSoft Package

