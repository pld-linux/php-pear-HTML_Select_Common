%include	/usr/lib/rpm/macros.php
%define		_class		HTML
%define		_subclass	Select
%define		_status		stable

%define		_pearname	%{_class}_%{_subclass}_Common
Summary:	%{_pearname} - small classes to handle common <select> lists
Summary(pl):	%{_pearname} - ma³e klasy do obs³ugi list <select>
Name:		php-pear-%{_pearname}
Version:	1.1
Release:	1
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	182210f08e809d51208ae4ecc70a4f3c
URL:		http://pear.php.net/package/%{_pearname}/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
Obsoletes:	php-pear-HTML_Select
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides <select>lists for:
 - Country
 - UK counties
 - US States

This class has in PEAR status: %{_status}.

%description -l pl
Dostarcza listy <select> do pytañ o:
 - kraj
 - kraje UK
 - stany US

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_subclass}/{,Common}

install %{_pearname}-%{version}/%{_subclass}/Common/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_subclass}/Common/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/%{_subclass}/Common/examples
%dir %{php_pear_dir}/%{_subclass}
%dir %{php_pear_dir}/%{_subclass}/Common
%{php_pear_dir}/%{_subclass}/Common/*.php
