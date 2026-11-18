import assert from "node:assert/strict";
import test from "node:test";
import { rewriteEngMode } from "../extensions/eng-mode.ts";

test("preserves multiline requests, quotes, spacing, and trailing content", () => {
	const request = ' Create config.yaml with exactly this content:\nserver:\n  title: "foo  bar"\n  port: 8080\n';
	assert.equal(rewriteEngMode("/eng-mode" + request), "/skill:eng-mode " + request);
});

test("preserves off, a bare command, and a newline or tab after the command", () => {
	for (const suffix of ["", " off", "\nInvestigate the failure", "\tFix it"]) {
		assert.equal(rewriteEngMode("/eng-mode" + suffix), "/skill:eng-mode " + suffix);
	}
});

test("leaves unrelated input and native skill commands unchanged", () => {
	for (const input of ["/eng-mode-extra task", "/eng-mode:1 task", "/skill:eng-mode task", "Explain /eng-mode", ""]) {
		assert.equal(rewriteEngMode(input), input);
	}
});
