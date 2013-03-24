%define _disable_ld_no_undefined 1

Summary:	X.org driver for NeoMagic Cards
Name:		x11-driver-video-neomagic
Version:	1.2.7
Release:	3
Group:		System/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-neomagic-%{version}.tar.bz2
Patch0:		remove_mibstore_h.patch

BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xorg-server)
BuildRequires:	pkgconfig(xproto)
Requires:	x11-server-common %(xserver-sdk-abi-requires videodrv)

%description
x11-driver-video-neomagic is the X.org driver for NeoMagic Cards.

%prep
%setup -qn xf86-video-neomagic-%{version}
%apply_patches

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%doc COPYING
%{_libdir}/xorg/modules/drivers/neomagic_drv.so
%{_mandir}/man4/neomagic.*

