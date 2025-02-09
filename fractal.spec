%global tarball_version %%(echo %{version} | tr '~' '.')

Name:           fractal
Version:        10
Release:        1
Summary:        GTK+ client for Matrix written in Rust
License:        GPL-3.0
Group:          Networking/Instant Messenger
URL:            https://wiki.gnome.org/Apps/Fractal
Source0:        https://gitlab.gnome.org/GNOME/fractal/-/archive/%{version}/%{name}-%{version}.tar.bz2
#Source0:        https://gitlab.gnome.org/World/fractal/-/releases/%{version}/downloads/tarball/fractal-%{version}.tar.xz
# Use vendor. Fractal developers should decide - they shipping tarball with vendored crates or not, and not just like now one release without and another with again again...
# Stop this madness. Also distributing rust packages and their dependencies is complete madness, and there is a need to provide vendor instead of linking to regular libraries like in any other civilized language. STOP THIS MADNESS
Source1:        vendor.tar.xz

# By default Fractal use rust crates that support only openssl v1 and not v3. While OpenMandriva provide devel only for v3.
# So let's force update few crates to latest that support openssl v3.
# Issue: https://gitlab.gnome.org/GNOME/fractal/-/issues/847
#Patch0:         fix-build-with-new-openssl3-openmandriva.patch

BuildRequires:  appstream
BuildRequires:  cargo
BuildRequires:  gmp-devel
BuildRequires:  meson
BuildRequires:  gettext
BuildRequires:  grass
BuildRequires:  pkgconfig
BuildRequires:  rust
BuildRequires:  pkgconfig(atk) >= 2.4
BuildRequires:  pkgconfig(cairo) >= 1.10
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gdk-3.0) >= 3.22
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= 2.30
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gspell-1) >= 1.8
BuildRequires:  pkgconfig(gst-editing-services-1.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-audio-1.0)
BuildRequires:  pkgconfig(gstreamer-bad-audio-1.0)
BuildRequires:  pkgconfig(gstreamer-base-1.0)
BuildRequires:  pkgconfig(gstreamer-player-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-bad-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gtksourceview-5)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(libseccomp)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(pango) >= 1.34
BuildRequires:  pkgconfig(pangocairo) >= 1.34
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(shumate-1.0)
BuildRequires:  pkgconfig(xdg-desktop-portal)
BuildRequires:  cmake(LLVM)
BuildRequires:	cmake(Clang)

%description
Fractal is a Matrix messaging app for GNOME written in GTK+ and Rust. Its
interface is tuned for collaboration in large groups, such as
free software projects.

%prep
%autosetup -p1 -a1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}

%files -f %{name}.lang
%license LICENSE*
%doc README.md
%{_bindir}/%{name}
%{_datadir}/metainfo/org.gnome.Fractal.metainfo.xml
%{_datadir}/applications/org.gnome.Fractal.desktop
%{_datadir}/icons/hicolor/*/apps/org.gnome.Fractal*.*
%{_datadir}/glib-2.0/schemas/org.gnome.Fractal.gschema.xml
%{_datadir}/fractal/resources.gresource
%{_datadir}/fractal/ui-resources.gresource
%{_datadir}/dbus-1/services/org.gnome.Fractal.service
