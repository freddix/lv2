Summary:	Plugin standard for audio systems
Name:		lv2
Version:	1.2.0
Release:	1
License:	LGPL v2.1 or later and BSD-like
Group:		Libraries
Source0:	http://lv2plug.in/spec/%{name}-%{version}.tar.bz2
# Source0-md5:	323b851563b4da1ad2c0faf5c76f0e3a
BuildRequires:	gtk+-devel
BuildRequires:	libsndfile-devel
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LV2 is a plugin standard for audio systems. It defines a minimal yet
extensible C API for plugin code and a format for plugin "bundles".

%package devel
Summary:	LV2 development files
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
LV2 development files.

%package examples
Summary:	Example LV2 plugins
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+

%description examples
Example LV2 plugins.

%prep
%setup -q

%build
export CC="%{__cc}"
export CXX="%{__cxx}"
export CFLAGS="%{rpmcflags}"
export CXXFLAGS="%{rpmcxxflags}"
./waf -v configure \
	--libdir=%{_libdir}	\
	--nocache		\
	--prefix=%{_prefix}
./waf -v

%install
rm -rf $RPM_BUILD_ROOT

./waf -v install	\
	--destdir=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir %{_libdir}/lv2
%dir %{_libdir}/lv2/*.lv2
%{_libdir}/lv2/*.lv2/*.ttl

%files devel
%defattr(644,root,root,755)
%dir %{_includedir}/lv2
%dir %{_includedir}/lv2/lv2plug.in
%dir %{_includedir}/lv2/lv2plug.in/ns

%dir %{_includedir}/lv2/lv2plug.in/ns/extensions
%{_includedir}/lv2/lv2plug.in/ns/extensions/ui
%{_includedir}/lv2/lv2plug.in/ns/extensions/units

%{_includedir}/lv2/lv2plug.in/ns/lv2core

%dir %{_includedir}/lv2/lv2plug.in/ns/ext
%{_includedir}/lv2/lv2plug.in/ns/ext/atom
%{_includedir}/lv2/lv2plug.in/ns/ext/buf-size
%{_includedir}/lv2/lv2plug.in/ns/ext/data-access
%{_includedir}/lv2/lv2plug.in/ns/ext/dynmanifest
%{_includedir}/lv2/lv2plug.in/ns/ext/event
%{_includedir}/lv2/lv2plug.in/ns/ext/instance-access
%{_includedir}/lv2/lv2plug.in/ns/ext/log
%{_includedir}/lv2/lv2plug.in/ns/ext/midi
%{_includedir}/lv2/lv2plug.in/ns/ext/morph
%{_includedir}/lv2/lv2plug.in/ns/ext/options
%{_includedir}/lv2/lv2plug.in/ns/ext/parameters
%{_includedir}/lv2/lv2plug.in/ns/ext/patch
%{_includedir}/lv2/lv2plug.in/ns/ext/port-groups
%{_includedir}/lv2/lv2plug.in/ns/ext/port-props
%{_includedir}/lv2/lv2plug.in/ns/ext/presets
%{_includedir}/lv2/lv2plug.in/ns/ext/resize-port
%{_includedir}/lv2/lv2plug.in/ns/ext/state
%{_includedir}/lv2/lv2plug.in/ns/ext/time
%{_includedir}/lv2/lv2plug.in/ns/ext/urid
%{_includedir}/lv2/lv2plug.in/ns/ext/uri-map
%{_includedir}/lv2/lv2plug.in/ns/ext/worker

%{_includedir}/lv2.h
%{_libdir}/lv2/*.lv2/*.c
%{_libdir}/lv2/*.lv2/*.h
%{_pkgconfigdir}/*.pc

%files examples
%defattr(644,root,root,755)
%dir %{_libdir}/lv2/eg-amp.lv2
%attr(755,root,root) %{_libdir}/lv2/eg-amp.lv2/amp.so
%{_libdir}/lv2/eg-amp.lv2/amp.ttl
%{_libdir}/lv2/eg-amp.lv2/manifest.ttl

%dir %{_libdir}/lv2/eg-sampler.lv2
%attr(755,root,root) %{_libdir}/lv2/eg-sampler.lv2/sampler.so
%{_libdir}/lv2/eg-sampler.lv2/click.wav
%{_libdir}/lv2/eg-sampler.lv2/manifest.ttl
%{_libdir}/lv2/eg-sampler.lv2/sampler.ttl
%{_libdir}/lv2/eg-sampler.lv2/sampler_ui.so

%dir %{_libdir}/lv2/eg-synth.lv2
%attr(755,root,root) %{_libdir}/lv2/eg-synth.lv2/synth.so
%{_libdir}/lv2/eg-synth.lv2/manifest.ttl
%{_libdir}/lv2/eg-synth.lv2/synth.ttl

