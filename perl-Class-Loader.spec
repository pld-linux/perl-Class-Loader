%include	/usr/lib/rpm/macros.perl
%define		pdir	Class
%define		pnam	Loader
Summary:	Class::Loader perl module
Summary(pl):	Modu³ perla Class::Loader
Name:		perl-Class-Loader
Version:	2.02
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a023ae4c71186fa4fc3e6bf5fe60b692
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Class::Loader Perl module - Load modules and create objects on demand.

%description -l pl
Modu³ Perla Class::Loader - wczytuj±cy modu³y i tworz±cy obiekty na
¿±danie.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Class/Loader.pm
%{_mandir}/man3/*
