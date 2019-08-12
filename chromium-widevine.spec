%global __strip /bin/true
%define debug_package %{nil}

Summary:        Plugin designed for the viewing of premium video content
Name:           chromium-widevine
Version:        4.10.1440.18
Release:        7%{?dist}

License:        Proprietary
Url:            http://www.google.com/chrome
Group:          Applications/Internet
Source0:	https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm
Source1:	http://www.google.com/chrome/intl/en/eula_text.html
Source2:	get_cdm_version.c

BuildRequires:  rpm cpio nss bc
BuildRequires:	gcc >= 5.1.1-2
ExclusiveArch:	x86_64
Obsoletes: chromium-pepper-flash-chromium-pdf-plugin

%description
A browser plugin designed for the viewing of premium video content.


%prep
%setup -c -T

%build

rpm2cpio %{S:0} | cpio -idmv

# We need see the version
pushd opt/google/chrome/
gcc %{S:2} -o get_cdm_version -ldl
./get_cdm_version > widevine_version
wv=$(cat widevine_version)
echo "version of widevine is $wv"

_output=`echo "$wv != %{version}" | bc`
if [[ $_output == "1" ]]; then
   echo "Version in source is not equal to %{version}"
exit 1
else
   echo "Version in source is equal to %{version}"
fi

%install

install -dm 755 %{buildroot}/usr/share/licenses/%{name}/
install -dm 755 %{buildroot}/%{_libdir}/chromium/
install -dm 755 %{buildroot}/%{_libdir}/chromium-browser

install -Dm644 opt/google/chrome/libwidevinecdm.so %{buildroot}/%{_libdir}/chromium/

# Really we need fix issues of other thirdparty repository?
ln -sf %{_libdir}/chromium/libwidevinecdm.so %{buildroot}/%{_libdir}/chromium-browser/libwidevinecdm.so

# License
install -m644 %{SOURCE1} %{buildroot}/%{_datadir}/licenses/%{name}/

%files
%{_libdir}/chromium/libwidevinecdm.so
%{_libdir}/chromium-browser/libwidevinecdm.so
%{_datadir}/licenses/%{name}/eula_text.html


%changelog

* Mon Aug 12 2019 David Vásquez <davidva AT tuta DOT io> - 4.10.1440.18-7
- Future problem solved

* Tue Jul 30 2019 David Vásquez <davidva AT tuta DOT io> - 4.10.1440.18-2
- Added detection of version in source

* Sun Jul 21 2019 David Vásquez <davidva AT tuta DOT io> - 4.10.1440.18-1
- Updated to 4.10.1440.18

* Wed Jan 09 2019 David Vásquez <davidva AT tuta DOT io> - 4.10.1224.7-1
- Updated to 4.10.1224.7

* Mon Oct 22 2018 David Vásquez <davidva AT tuta DOT io> - 4.10.1196.0-1
- Updated to 4.10.1196.0

* Thu Sep 06 2018 David Vásquez <davidva AT tuta DOT io> - 4.10.1192.0-1
- Updated to 4.10.1192.0

* Wed Jul 25 2018 David Vásquez <davidva AT tutanota DOT com> - 4.10.1146.0-1
- Updated to 4.10.1146.0

* Tue May 29 2018 David Vásquez <davidva AT tutanota DOT com> - 1.4.9.1088-1
- Updated to 1.4.9.1088

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
