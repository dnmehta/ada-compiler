#Reserved Token Definitions for Ada Language

#These literals are taken from http://en.wikibooks.org/wiki/Ada_Programming/All_Keywords
#Some of them are for specific Ada verisons, we are designing a compiler for Ada 2012 but are still including all the special words in Ada

reserved = {
	'abort':'ABORT',
	'abs':'ABS',
	'abstract':'ABSTRACT',
	'accept':'ACCEPT',
	'access':'ACCESS',
	'aliased':'ALIASED',
	'all':'ALL',
	'and':'AND',
	'array':'ARRAY',
	'at':'AT',
	'begin':'BEGIN',
	'body':'BODY',
	'case':'CASE',
	'constant':'CONSTANT',
	'declare':'DECLARE',
	'delay':'DELAY',
	'delta':'DELTA',
	'digits':'DIGITS',
	'do':'DO',
	'else':'ELSE',
	'elsif':'ELSIF',
	'end':'END',
	'entry':'ENTRY',
	'exception':'EXCEPTION',
	'exit':'EXIT',
	'for':'FOR',
	'function':'FUNCTION',
	'generic':'GENERIC',
	'goto':'GOTO',
	'if':'IF',
	'in':'IN',
	'interface':'INTERFACE',
	'is':'IS',
	'limited':'LIMITED',
	'loop':'LOOP',
	'mod':'MOD',
	'new':'NEW',
	'not':'NOT',
	'null':'NuLL',
	'of':'OF',
	'or':'OR',
	'others':'OTHERS',
	'out':'OUT',
	'overriding':'OVERRIDING',
	'package':'PACKAGE',
	'pragma':'PRAGMA',
	'private':'PRIVATE',
	'procedure':'PROCEDURE',
	'protected':'PROTECTED',
	'raise':'RAISE',
	'range':'RANGE',
	'record':'RECORD',
	'rem':'REM',
	'renames':'RENAMES',
	'requeue':'REQUEUE',
	'return':'RETURN',
	'reverse':'REVERSE',
	'select':'SELECT',
	'separate':'SEPARATE',
	'some':'SOME',
	'subtype':'SUBTYPE',
	'synchronized':'SYNCHRONIZED',
	'tagged':'TAGGED',
	'task':'TASK',
	'terminate':'TERMINATE',
	'then':'THEN',
	'type':'TYPE',
	'until':'UNTIL',
	'use':'USE',
	'when':'WHEN',
	'while':'WHILE',
	'with':'WITH',
	'xor':'XOR',
	
	#Attributes - These are taken by parsing http://en.wikibooks.org/wiki/Ada_Programming/Attributes
	'\'Access':'ATTR_ACCESS',
	'\'Address':'ATTR_ADDRESS',
	'\'Adjacent':'ATTR_ADJACENT',
	'\'Aft':'ATTR_AFT',
	'\'Alignment':'ATTR_ALIGNMENT',
	'\'Base':'ATTR_BASE',
	'\'Bit_Order':'ATTR_BIT_ORDER',
	'\'Body_Version':'ATTR_BODY_VERSION',
	'\'Callable':'ATTR_CALLABLE',
	'\'Caller':'ATTR_CALLER',
	'\'Ceiling':'ATTR_CEILING',
	'\'Class':'ATTR_CLASS',
	'\'Component_Size':'ATTR_COMPONENT_SIZE',
	'\'Compose':'ATTR_COMPOSE',
	'\'Constrained':'ATTR_CONSTRAINED',
	'\'Copy_Sign':'ATTR_COPY_SIGN',
	'\'Count':'ATTR_COUNT',
	'\'Definite':'ATTR_DEFINITE',
	'\'Delta':'ATTR_DELTA',
	'\'Denorm':'ATTR_DENORM',
	'\'Digits':'ATTR_DIGITS',
	'\'Exponent':'ATTR_EXPONENT',
	'\'External_Tag':'ATTR_EXTERNAL_TAG',
	'\'Epsilon':'ATTR_EPSILON',
	'\'First':'ATTR_FIRST',
	'\'First_Bit':'ATTR_FIRST_BIT',
	'\'Floor':'ATTR_FLOOR',
	'\'Fore':'ATTR_FORE',
	'\'Fraction':'ATTR_FRACTION',
	'\'Has_Same_Storage':'ATTR_HAS_SAME_STORAGE',
	'\'Identity':'ATTR_IDENTITY',
	'\'Image':'ATTR_IMAGE',
	'\'Input':'ATTR_INPUT',
	'\'Large':'ATTR_LARGE',
	'\'Last':'ATTR_LAST',
	'\'Last_Bit':'ATTR_LAST_BIT',
	'\'Leading_Part':'ATTR_LEADING_PART',
	'\'Length':'ATTR_LENGTH',
	'\'Machine':'ATTR_MACHINE',
	'\'Machine_Emax':'ATTR_MACHINE_EMAX',
	'\'Machine_Emin':'ATTR_MACHINE_EMIN',
	'\'Machine_Mantissa':'ATTR_MACHINE_MANTISSA',
	'\'Machine_Overflows':'ATTR_MACHINE_OVERFLOWS',
	'\'Machine_Radix':'ATTR_MACHINE_RADIX',
	'\'Machine_Rounding':'ATTR_MACHINE_ROUNDING',
	'\'Machine_Rounds':'ATTR_MACHINE_ROUNDS',
	'\'Mantissa':'ATTR_MANTISSA',
	'\'Max':'ATTR_MAX',
	'\'Max_Aligment_For_Allocation':'ATTR_MAX_ALIGMENT_FOR_ALLOCATION',
	'\'Max_Size_In_Storage_Elements':'ATTR_MAX_SIZE_IN_STORAGE_ELEMENTS',
	'\'Min':'ATTR_MIN',
	'\'Mod':'ATTR_MOD',
	'\'Model':'ATTR_MODEL',
	'\'Model_Emin':'ATTR_MODEL_EMIN',
	'\'Model_Epsilon':'ATTR_MODEL_EPSILON',
	'\'Model_Mantissa':'ATTR_MODEL_MANTISSA',
	'\'Model_Small':'ATTR_MODEL_SMALL',
	'\'Modulus':'ATTR_MODULUS',
	'\'Old':'ATTR_OLD',
	'\'Output':'ATTR_OUTPUT',
	'\'Overlaps_Storage':'ATTR_OVERLAPS_STORAGE',
	'\'Partition_ID':'ATTR_PARTITION_ID',
	'\'Pos':'ATTR_POS',
	'\'Position':'ATTR_POSITION',
	'\'Pred':'ATTR_PRED',
	'\'Priority':'ATTR_PRIORITY',
	'\'Range':'ATTR_RANGE',
	'\'Read':'ATTR_READ',
	'\'Remainder':'ATTR_REMAINDER',
	'\'Result':'ATTR_RESULT',
	'\'Round':'ATTR_ROUND',
	'\'Rounding':'ATTR_ROUNDING',
	'\'Safe_Emax':'ATTR_SAFE_EMAX',
	'\'Safe_First':'ATTR_SAFE_FIRST',
	'\'Safe_Large':'ATTR_SAFE_LARGE',
	'\'Safe_Last':'ATTR_SAFE_LAST',
	'\'Safe_Small':'ATTR_SAFE_SMALL',
	'\'Scale':'ATTR_SCALE',
	'\'Scaling':'ATTR_SCALING',
	'\'Signed_Zeros':'ATTR_SIGNED_ZEROS',
	'\'Size':'ATTR_SIZE',
	'\'Small':'ATTR_SMALL',
	'\'Storage_Pool':'ATTR_STORAGE_POOL',
	'\'Storage_Size':'ATTR_STORAGE_SIZE',
	'\'Stream_Size':'ATTR_STREAM_SIZE',
	'\'Succ':'ATTR_SUCC',
	'\'Tag':'ATTR_TAG',
	'\'Terminated':'ATTR_TERMINATED',
	'\'Truncation':'ATTR_TRUNCATION',
	'\'Unbiased_Rounding':'ATTR_UNBIASED_ROUNDING',
	'\'Unchecked_Access':'ATTR_UNCHECKED_ACCESS',
	'\'Val':'ATTR_VAL',
	'\'Valid':'ATTR_VALID',
	'\'Value':'ATTR_VALUE',
	'\'Version':'ATTR_VERSION',
	'\'Wide_Image':'ATTR_WIDE_IMAGE',
	'\'Wide_Value':'ATTR_WIDE_VALUE',
	'\'Wide_Wide_Image':'ATTR_WIDE_WIDE_IMAGE',
	'\'Wide_Wide_Value':'ATTR_WIDE_WIDE_VALUE',
	'\'Wide_Wide_Width':'ATTR_WIDE_WIDE_WIDTH',
	'\'Wide_Width':'ATTR_WIDE_WIDTH',
	'\'Width':'ATTR_WIDTH',
	'\'Write':'ATTR_WRITE'
}
