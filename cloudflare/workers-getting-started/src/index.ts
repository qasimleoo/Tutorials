/**
 * Welcome to Cloudflare Workers! This is your first worker.
 *
 * - Run `npm run dev` in your terminal to start a development server
 * - Open a browser tab at http://localhost:8787/ to see your worker in action
 * - Run `npm run deploy` to publish your worker
 *
 * Bind resources to your worker in `wrangler.jsonc`. After adding bindings, a type definition for the
 * `Env` object can be regenerated with `npm run cf-typegen`.
 *
 * Learn more at https://developers.cloudflare.com/workers/
 */

// export default {
	
// 	async fetch(request, env, ctx): Promise<Response> {

// 		console.log("Logging info")
// 		console.log(JSON.stringify(request.cf));

// 		const url = new URL(request.url);
// 		switch (url.pathname) {
// 			case '/message':
// 				return new Response('Hello, World!');
// 			case '/random':
// 				return new Response(crypto.randomUUID());
// 			default:
// 				return new Response('Not Found', { status: 404 });
// 		}
// 	},
// } satisfies ExportedHandler<Env>;


// Hono

import { Hono } from 'hono'
import { Ai } from "@cloudflare/ai"

export interface Env{
	AI: any
}

const app = new Hono<{'Bindings': Env}>()

app.get('/message', async (c) => {
	const ai = new Ai(c.env.AI)

	const messages = [
		{ role: "system", content: "You are a frsongsiendly assistant" },
		{
			role: "user",
			content: "What is the origin of the phrase Hello, World",
		},
    ];

	// const stream = await env.AI.run("@cf/deepseek-ai/deepseek-r1-distill-qwen-32b", {
	// 	messages,
	// 	stream: true,
    // });

	const inputs = { messages }

	const res = await ai.run("@cf/mistral/mistral-7b-instruct-v0.1", inputs)

	return c.json(res)
})

app.post('/ai', async (c) => {
	const { prompt } = await c.req.json()

	let result

	if (c.env.AI) {
		// Production: use Cloudflare AI service
		result = await c.env.AI.chat.completions.create({
			model: 'gpt-4o-mini',
			messages: [{ role: 'user', content: prompt }],
			max_tokens: 100
		})
	} else {
    // Local dev: mock response
    result = {
		id: 'local-mock',
		choices: [{ message: { role: 'assistant', content: `Echo: ${prompt}` } }]
    }
	}

	return c.json(result)
})

app.get('/random', (c) => {
	return c.text(crypto.randomUUID())
})

export default app