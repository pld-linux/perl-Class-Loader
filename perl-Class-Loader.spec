#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Class
%define		pnam	Loader
Summary:	Class::Loader - load modules and create objects on demand
Summary(pl):	Class::Loader - wczytywanie modu³ów i tworzenie obiektów na ¿±danie
Name:		perl-Class-Loader
Version:	2.02
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a023ae4c71186fa4fc3e6bf5fe60b692
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Class::Loader is an inheritable class that provides a method, _load(),
to load a module from disk and construct an object by calling its
constructor.

%description -l pl
Class::Loader jest dziedziczon± klas± udostêpniaj±c± metodê _load(),
s³u¿±c± do wczytania modu³u z dysku i stworzenia obiektu poprzez
wywo³anie jego konstruktora.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Class/Loader.pm
%{_mandir}/man3/*
