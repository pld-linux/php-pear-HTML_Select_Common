%include	/usr/lib/rpm/macros.php
%define		_class		HTML
%define		_subclass	Select
%define		_status		stable

%define		_pearname	%{_class}_%{_subclass}_Common
Summary:	%{_pearname} - small classes to handle common <select> lists
Summary(pl.UTF-8):	%{_pearname} - małe klasy do obsługi list <select>
Name:		php-pear-%{_pearname}
Version:	1.1
Release:	4
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	182210f08e809d51208ae4ecc70a4f3c
URL:		http://pear.php.net/package/HTML_Select_Common/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-I18N >= 0.8
Obsoletes:	php-pear-HTML_Select
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides <select>lists for:
 - Country
 - UK counties
 - US States

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Dostarcza listy <select> do pytań o:
 - kraj
 - kraje UK
 - stany US

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

mkdir -p docs/%{_pearname}
mv ./%{php_pear_dir}/%{_class}/%{_subclass}/Common/examples docs/%{_pearname}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/examples
%{php_pear_dir}/.registry/*.reg
%dir %{php_pear_dir}/%{_class}/%{_subclass}
%dir %{php_pear_dir}/%{_class}/%{_subclass}/Common
%{php_pear_dir}/%{_class}/%{_subclass}/Common/*.php
