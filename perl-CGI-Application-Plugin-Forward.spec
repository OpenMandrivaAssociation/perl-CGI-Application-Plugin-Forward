%define module   CGI-Application-Plugin-Forward
%define version    1.06
%define release    %mkrel 1

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Pass control from one run mode to another
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/CGI/%{module}-%{version}.tar.gz
BuildRequires: perl(CGI::Application)
BuildRequires: perl(Test::More)
BuildRequires: perl(Module::Build::Compat)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

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
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/man3/*
%perl_vendorlib/CGI

