%define upstream_name    CGI-Application-Plugin-Forward
%define upstream_version 1.06

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Pass control from one run mode to another
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/CGI/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(CGI::Application)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Module::Build::Compat)
BuildArch:	noarch

%description
The forward method passes control to another run mode and returns its
output. This is equivalent to calling '$self->$other_runmode', except that
the CGI::Application manpage's internal value of the current run mode is
updated.

This means that calling '$self->get_current_runmode' after calling
'forward' will return the name of the new run mode. This is useful for
modules that depend on the name of the current run mode such as the
CGI::Application::Plugin::AnyTemplate manpage.

For example, here's how to pass control to a run mode named 'other_action'
from 'start' while updating the value of 'current_run_mode':

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README Changes
%{_mandir}/man3/*
%{perl_vendorlib}/CGI


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 1.60.0-2mdv2011.0
+ Revision: 680681
- mass rebuild

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 1.60.0-1mdv2011.0
+ Revision: 405775
- rebuild using %%perl_convert_version

* Wed Nov 26 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.06-1mdv2009.1
+ Revision: 307042
- import perl-CGI-Application-Plugin-Forward


* Wed Nov 26 2008 cpan2dist 1.06-1mdv
- initial mdv release, generated with cpan2dist

