Name:		python-posthog
Version:	7.53.0
Release:	1
Summary:	PostHog Python analytics SDK
License:	MIT
Group:		Development/Python
URL:		https://github.com/PostHog/posthog-python
Source0:	https://files.pythonhosted.org/packages/source/p/posthog/posthog-%{version}.tar.gz
BuildArch:	noarch
BuildSystem:	python
BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
Requires:	python%{pyver}dist(requests)
Requires:	python%{pyver}dist(backoff)
Requires:	python%{pyver}dist(distro)

%description
Official PostHog Python library. Aider uses it for optional telemetry.

%files
%doc README.md
%license LICENSE
%{py_sitedir}/posthog
%{py_sitedir}/posthog-*.*-info
