.PHONY: spec generate test verify

spec:
	python3 scripts/build_spec.py

generate: spec
	./scripts/generate.sh

test:
	python3 -m pytest scripts/test_build_spec.py -v
	go test ./... 

# Proves the committed SDK equals upstream + overlay + templates.
verify: generate
	git diff --exit-code || (echo "ERROR: committed SDK differs from regenerated output" && exit 1)
