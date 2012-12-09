Name: x11-driver-video-neomagic
Version: 1.2.7
Release: 2
Summary: X.org driver for NeoMagic Cards
Group: System/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/driver/xf86-video-neomagic-%{version}.tar.bz2

BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.12
BuildRequires: x11-util-macros >= 1.0.1
Conflicts: xorg-x11-server < 7.0

%description
x11-driver-video-neomagic is the X.org driver for NeoMagic Cards.

%prep
%setup -qn xf86-video-neomagic-%{version}

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%files
%doc COPYING
%{_libdir}/xorg/modules/drivers/neomagic_drv.so
%{_mandir}/man4/neomagic.*



%changelog
* Mon Jul 23 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.2.7-1
+ Revision: 810707
- version update 1.2.7

* Tue Mar 27 2012 Bernhard Rosenkraenzer <bero@bero.eu> 1.2.6-2
+ Revision: 787234
- Rebuild for x11-server 1.12

* Sun Mar 25 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.2.6-1
+ Revision: 786714
- version update 1.2.6

* Sat Dec 31 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.2.5-6
+ Revision: 748428
- rebuild cleaned up spec

* Sat Oct 08 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 1.2.5-5
+ Revision: 703684
- rebuild for new x11-server

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2.5-4
+ Revision: 671155
- mass rebuild

* Sun Oct 10 2010 Thierry Vignaud <tv@mandriva.org> 1.2.5-3mdv2011.0
+ Revision: 584626
- bump release before rebuilding for xserver 1.9

* Tue Jul 20 2010 Thierry Vignaud <tv@mandriva.org> 1.2.5-2mdv2011.0
+ Revision: 556290
- drop patch 0 (merged upstream)
- new release

* Thu Jan 28 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.2.4-2mdv2010.1
+ Revision: 497571
- Add a patch to solve unresolved symbols

* Mon Aug 03 2009 Thierry Vignaud <tv@mandriva.org> 1.2.4-1mdv2010.0
+ Revision: 407741
- new release

* Fri Jul 03 2009 Ander Conselvan de Oliveira <ander@mandriva.com> 1.2.3-1mdv2010.0
+ Revision: 391883
- update to new version 1.2.3

* Tue Dec 30 2008 Colin Guthrie <cguthrie@mandriva.org> 1.2.2-2mdv2009.1
+ Revision: 321381
- Rebuild for new xserver

* Tue Dec 23 2008 Ander Conselvan de Oliveira <ander@mandriva.com> 1.2.2-1mdv2009.1
+ Revision: 317848
- New version 1.2.2

* Sat Nov 29 2008 Adam Williamson <awilliamson@mandriva.org> 1.2.1-3mdv2009.1
+ Revision: 308169
- rebuild for new X server

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 1.2.1-2mdv2009.0
+ Revision: 265924
- rebuild early 2009.0 package (before pixel changes)
- improved description
- fix group
- add missing dot at end of description
- improved summary

* Tue May 27 2008 Colin Guthrie <cguthrie@mandriva.org> 1.2.1-1mdv2009.0
+ Revision: 211782
- New version

* Tue Apr 15 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.2.0-1mdv2009.0
+ Revision: 194167
- Update to version 1.2.0.

* Mon Feb 11 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.1.1-7mdv2008.1
+ Revision: 165571
- Revert to use upstream tarball and remove local patches.

* Tue Jan 22 2008 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.1.1-6mdv2008.1
+ Revision: 156611
- re-enable rpm debug packages support

* Fri Jan 18 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.1.1-5mdv2008.1
+ Revision: 154845
- Updated BuildRequires and resubmit package.
- Remove -devel package as it isn't really required as it provides only 2 files
  that aren't even header files; still don't install the .la files.
  All dependency files should be stored in the x11-util-modular package as they
  are only required for the "modular" build.
- Move .la files to new -devel package, and also add .deps files to -devel package.
- Note local tag xf86-video-cyrix-1.1.0@mandriva suggested on upstream
  Tag at git checkout afedccae164668128c6228542585cc27d241b7e6
- Update for new policy of hidden symbols and common macros.

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 15 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.1.1-4mdv2008.1
+ Revision: 98698
- minor spec cleanup
- build against new xserver (1.4)

* Thu Aug 30 2007 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-3mdv2008.0
+ Revision: 75775
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - fix man pages

