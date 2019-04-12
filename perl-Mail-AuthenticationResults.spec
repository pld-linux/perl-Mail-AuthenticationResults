#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Mail
%define		pnam	AuthenticationResults
%include	/usr/lib/rpm/macros.perl
Summary:	Mail::AuthenticationResults - Object Oriented Authentication-Results Headers
Name:		perl-Mail-AuthenticationResults
Version:	1.20180923
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Mail/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d4ca126d3af0d1b664249f93bdd021f0
URL:		https://metacpan.org/release/Mail-AuthenticationResults/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-Exception
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Object Oriented Authentication-Results email headers.

This parser copes with most styles of Authentication-Results header
seen in the wild, but is not yet fully RFC7601 compliant

Differences from RFC7601

key/value pairs are parsed when present in the authserv-id section,
this is against RFC but has been seen in headers added by Yahoo!.

Comments added between key/value pairs will be added after them in the
data structures and when stringified.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Mail/*.pm
%{perl_vendorlib}/Mail/AuthenticationResults
%{_mandir}/man3/*
