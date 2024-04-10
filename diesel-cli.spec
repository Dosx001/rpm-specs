Name: diesel-cli
Version: 2.1.5
Release: 1%{?dist}
Summary: CLI for the Diesel crate
license: MIT
BuildRequires: cargo libpq-devel
Requires: postgresql-server
URL: https://github.com/diesel-rs/diesel
Source0: https://github.com/diesel-rs/diesel/archive/v%{version}/diesel-%{version}.tar.gz

%global debug_package %{nil}

%description
Diesel CLI is a tool that aids in managing your database schema. Migrations are
bi-directional changes to your database that get applied sequentially

%pprep
%setup -q -n diesel-%{version}/diesel_cli
touch Cargo.lock
# cargo fetch --target "%{_arch}-unknown-linux-gnu"
# cargo update -p clap@4.5.4 --precise 4.4.18
# cargo update -p clap_complete@4.5.1 --precise 4.4.10

%build
cargo build --release --no-default-features --features postgres --locked

%install
cd ..
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -D -m 755 target/release/diesel %{buildroot}%{_bindir}/diesel

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/diesel
