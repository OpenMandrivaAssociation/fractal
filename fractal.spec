Name:           fractal
Version:        4.4.1b1
Release:        1
Summary:        GTK+ client for Matrix written in Rust
License:        GPL-3.0
Group:          Networking/Instant Messenger
URL:            https://wiki.gnome.org/Apps/Fractal
Source0:        https://gitlab.gnome.org/GNOME/fractal/-/archive/%{version}/%{name}-%{version}.tar.bz2

BuildRequires:  cargo
BuildRequires:  gmp-devel
BuildRequires:  meson
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
BuildRequires:  pkgconfig(gtk+-3.0)  >= 3.22
BuildRequires:  pkgconfig(gtksourceview-4) >= 4.0
BuildRequires:  pkgconfig(libhandy-0.0) >= 0.0.5
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(pango) >= 1.34
BuildRequires:  pkgconfig(pangocairo) >= 1.34

%description
Fractal is a Matrix messaging app for GNOME written in GTK+ and Rust. Its
interface is tuned for collaboration in large groups, such as
free software projects.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}

%files
%license LICENSE.txt
%doc README.md
%{_bindir}/%{name}
%{_datadir}/metainfo/org.gnome.Fractal.metainfo.xml
%{_datadir}/applications/org.gnome.Fractal.desktop
%{_datadir}/icons/hicolor/*/apps/org.gnome.Fractal*.*
%{_datadir}/glib-2.0/schemas/org.gnome.Fractal.gschema.xml

%files lang -f %{name}.lang
