import type { ExtensionAPI } from "@earendil-works/pi-coding-agent";

export function rewriteEngMode(text: string): string {
	return text.replace(/^\/eng-mode(?=\s|$)/, "/skill:eng-mode ");
}

export default function (pi: ExtensionAPI) {
	pi.on("input", (event) => {
		const text = rewriteEngMode(event.text);
		if (text === event.text) return { action: "continue" };
		return { action: "transform", text, images: event.images };
	});
}
