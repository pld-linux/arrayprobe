Summary:	Arrayprobe - reporting the status of HP/Compaq array controller
Summary(pl.UTF-8):	Arrayprobe - informowanie o stanie kontrolerów macierzowych HP/Compaq
Name:		arrayprobe
Version:	2.0
Release:	0.1
License:	GPL v2+
Group:		Applications/System
Source0:	http://www.strocamp.net/opensource/compaq/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	7300f24a712265fd7430c6b48bd1dd75
Patch0:		%{name}-headers.patch
URL:		http://www.strocamp.net/opensource/arrayprobe.php
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Arrayprobe is a Linux commandline utility that reports the status of a
HP/Compaq array controller.

%description -l pl.UTF-8
Arrayprobe to linuksowe narzędzie działające z linii poleceń
informujące o stanie kontrolerów macierzowych HP/Compaq.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/arrayprobe
