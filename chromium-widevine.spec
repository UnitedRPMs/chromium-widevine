%define debug_package %{nil}

Summary:        Plugin designed for the viewing of premium video content
Name:           chromium-widevine
Version:        1.4.9.1076
Release:        1%{?dist}

License:        Proprietary
Url:            http://www.google.com/chrome
Group:          Applications/Internet
Source:		http://www.google.com/chrome/intl/en/eula_text.html

BuildRequires:  rpm cpio wget
ExclusiveArch:	x86_64
Obsoletes: chromium-pepper-flash-chromium-pdf-plugin

%description
A browser plugin designed for the viewing of premium video content.


%prep
%setup -c -T
wget -c -P %{_builddir}/%{name}-%{version} https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm


%build

rpm2cpio %{_builddir}/%{name}-%{version}/google-chrome-stable_current_x86_64.rpm | cpio -idmv



%install

install -dm 755 %{buildroot}/usr/share/licenses/%{name}/
install -dm 755 %{buildroot}/%{_libdir}/chromium/

install -Dm644 opt/google/chrome/libwidevinecdm.so %{buildroot}/%{_libdir}/chromium/
install -Dm644 opt/google/chrome/libwidevinecdmadapter.so %{buildroot}/%{_libdir}/chromium/

# License
install -m644 %{SOURCE0} %{buildroot}/%{_datadir}/licenses/%{name}/

%files
%{_libdir}/chromium/libwidevinecdm.so
%{_libdir}/chromium/libwidevinecdmadapter.so
%{_datadir}/licenses/%{name}/eula_text.html


%changelog

* Wed Apr 18 2018 David Vásquez <davidva AT tutanota DOT com> - 1.4.9.1076-1
- Updated to 1.4.9.1076

* Wed Jan 24 2018 David Vásquez <davidva AT tutanota DOT com> - 1.4.9.1070-1
- Updated to 1.4.9.1070

* Thu Nov 16 2017 David Vásquez <davidva AT tutanota DOT com> - 1.4.8.1029-1
- Updated to 1.4.8.1029

* Sun Sep 10 2017 David Vásquez <davidva AT tutanota DOT com> - 1.4.8.1008-1
- Updated to 1.4.8.1008

* Mon Jul 10 2017 David Vásquez <davidva AT tutanota DOT com> - 1.4.8.977-1
- Updated to 1.4.8.977

* Sat Mar 18 2017 David Vásquez <davidva AT tutanota DOT com> - 1.4.8.970-1
- Updated to 1.4.8.970

* Fri Mar 03 2017 David Vásquez <davidva AT tutanota DOT com> - 1.4.8.962-2
- Solved conflict with widevine in official package

* Thu Mar 02 2017 David Vásquez <davidva AT tutanota DOT com> - 1.4.8.962-1
- Udated to 1.4.8.962

* Wed Jan 04 2017 David Vásquez <davidva AT tutanota DOT com> - 1.4.8.903-1
- Updated to 1.4.8.903

* Fri Jul 29 2016 David Vásquez <davidva AT tutanota DOT com> - 1.4.8.893-1
- Updated to 1.4.8.893

* Tue Jun 21 2016 David Vásquez <davidva AT tutanota DOT com> - 1.4.8.885-2
- Compatibility with chromium-bin

* Wed Jun 15 2016 David Vásquez <davidva AT tutanota DOT com> - 1.4.8.885-1
- initial build 
