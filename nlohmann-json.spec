Name: nlohmann-json
Version: 3.11.3
Release: 1%{?dist}
Summary:  JSON for Modern C++
License: MIT
URL: https://json.nlohmann.me
Source0: https://github.com/nlohmann/json/archive/v%{version}/json-%{version}.tar.gz
BuildRequires: cmake make

%global debug_package %{nil}

%description
C++ library for JSON serialization and deserialization.

%prep
%setup -q -n json-%{version}
cmake CMakeLists.txt

%build
make -j 10

%install
%make_install

%files
/usr/local/include/nlohmann/adl_serializer.hpp
/usr/local/include/nlohmann/byte_container_with_subtype.hpp
/usr/local/include/nlohmann/detail/abi_macros.hpp
/usr/local/include/nlohmann/detail/conversions/from_json.hpp
/usr/local/include/nlohmann/detail/conversions/to_chars.hpp
/usr/local/include/nlohmann/detail/conversions/to_json.hpp
/usr/local/include/nlohmann/detail/exceptions.hpp
/usr/local/include/nlohmann/detail/hash.hpp
/usr/local/include/nlohmann/detail/input/binary_reader.hpp
/usr/local/include/nlohmann/detail/input/input_adapters.hpp
/usr/local/include/nlohmann/detail/input/json_sax.hpp
/usr/local/include/nlohmann/detail/input/lexer.hpp
/usr/local/include/nlohmann/detail/input/parser.hpp
/usr/local/include/nlohmann/detail/input/position_t.hpp
/usr/local/include/nlohmann/detail/iterators/internal_iterator.hpp
/usr/local/include/nlohmann/detail/iterators/iter_impl.hpp
/usr/local/include/nlohmann/detail/iterators/iteration_proxy.hpp
/usr/local/include/nlohmann/detail/iterators/iterator_traits.hpp
/usr/local/include/nlohmann/detail/iterators/json_reverse_iterator.hpp
/usr/local/include/nlohmann/detail/iterators/primitive_iterator.hpp
/usr/local/include/nlohmann/detail/json_custom_base_class.hpp
/usr/local/include/nlohmann/detail/json_pointer.hpp
/usr/local/include/nlohmann/detail/json_ref.hpp
/usr/local/include/nlohmann/detail/macro_scope.hpp
/usr/local/include/nlohmann/detail/macro_unscope.hpp
/usr/local/include/nlohmann/detail/meta/call_std/begin.hpp
/usr/local/include/nlohmann/detail/meta/call_std/end.hpp
/usr/local/include/nlohmann/detail/meta/cpp_future.hpp
/usr/local/include/nlohmann/detail/meta/detected.hpp
/usr/local/include/nlohmann/detail/meta/identity_tag.hpp
/usr/local/include/nlohmann/detail/meta/is_sax.hpp
/usr/local/include/nlohmann/detail/meta/std_fs.hpp
/usr/local/include/nlohmann/detail/meta/type_traits.hpp
/usr/local/include/nlohmann/detail/meta/void_t.hpp
/usr/local/include/nlohmann/detail/output/binary_writer.hpp
/usr/local/include/nlohmann/detail/output/output_adapters.hpp
/usr/local/include/nlohmann/detail/output/serializer.hpp
/usr/local/include/nlohmann/detail/string_concat.hpp
/usr/local/include/nlohmann/detail/string_escape.hpp
/usr/local/include/nlohmann/detail/value_t.hpp
/usr/local/include/nlohmann/json.hpp
/usr/local/include/nlohmann/json_fwd.hpp
/usr/local/include/nlohmann/ordered_map.hpp
/usr/local/include/nlohmann/thirdparty/hedley/hedley.hpp
/usr/local/include/nlohmann/thirdparty/hedley/hedley_undef.hpp
/usr/local/include/test_data.hpp
/usr/local/share/cmake/nlohmann_json/nlohmann_jsonConfig.cmake
/usr/local/share/cmake/nlohmann_json/nlohmann_jsonConfigVersion.cmake
/usr/local/share/cmake/nlohmann_json/nlohmann_jsonTargets.cmake
/usr/local/share/pkgconfig/nlohmann_json.pc
