import { app } from "../scripts/app.js";

const ext = {
	name: "pysssss.LinkRenderMode",
	async setup(app) {
		app.canvas.links_render_mode = 0;
	}
};

app.registerExtension(ext);
