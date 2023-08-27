# Makefile

# Testleri çalıştırmak için kullanacağımız komut
TEST_CMD := pre-commit run -a

# Test komutunu çalıştırır
test:
	$(TEST_CMD)

# Varsayılan hedefi 'test' olarak ayarla
.DEFAULT_GOAL := test
