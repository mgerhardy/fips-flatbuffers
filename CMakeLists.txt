fips_begin_app(flatc cmdline)
	fips_files(
		flatbuffers/include/flatbuffers/flatbuffers.h
		flatbuffers/include/flatbuffers/idl.h
		flatbuffers/include/flatbuffers/util.h
		flatbuffers/src/idl_parser.cpp
		flatbuffers/src/idl_gen_cpp.cpp
		flatbuffers/src/idl_gen_general.cpp
		flatbuffers/src/idl_gen_go.cpp
		flatbuffers/src/idl_gen_text.cpp
		flatbuffers/src/idl_gen_fbs.cpp
		flatbuffers/src/flatc.cpp
	)
fips_end_app()
