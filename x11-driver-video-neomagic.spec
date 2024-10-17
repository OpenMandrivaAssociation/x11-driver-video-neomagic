%define _disable_ld_no_undefined 1

Summary:	X.org driver for NeoMagic Cards
Name:		x11-driver-video-neomagic
Version:	1.3.1
Release:	1
Group:		System/X11
License:	MIT
Url:		https://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-neomagic-%{version}.tar.xz
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xorg-server)
BuildRequires:	pkgconfig(xproto)
Requires:	x11-server-common %(xserver-sdk-abi-requires videodrv)

%description
x11-driver-video-neomagic is the X.org driver for NeoMagic Cards.

%prep
%setup -qn xf86-video-neomagic-%{version}
%autopatch -p1

%build
%configure
%make

%install
%makeinstall_std

%files
%doc COPYING
%{_libdir}/xorg/modules/drivers/neomagic_drv.so
%{_mandir}/man4/neomagic.*

