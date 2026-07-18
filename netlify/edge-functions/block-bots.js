// Hard-blocks crawlers that are known to ignore robots.txt (Bytespider,
// PetalBot, SEO scrapers) plus the AI-training bots already disallowed in
// robots.txt. Search engines (Googlebot, bingbot, DuckDuckBot) are never
// matched, so SEO and Google Scholar indexing are unaffected.
const BLOCKED_UA =
  /bytespider|tiktokspider|petalbot|semrushbot|ahrefsbot|mj12bot|dotbot|dataforseo|blexbot|zoominfobot|barkrowler|serpstatbot|seekportbot|megaindex|mauibot|gptbot|ccbot|claudebot|claude-web|anthropic-ai|amazonbot|meta-external|facebookbot|diffbot|omgili|imagesift|ai2bot|timpibot|pangubot|cohere|scrapy/i;

export default async (request, context) => {
  const { pathname } = new URL(request.url);

  // Bots must always be able to read robots.txt.
  if (pathname === "/robots.txt") {
    return context.next();
  }

  const ua = request.headers.get("user-agent") || "";
  if (BLOCKED_UA.test(ua)) {
    return new Response("Forbidden", {
      status: 403,
      headers: { "cache-control": "no-store" },
    });
  }

  return context.next();
};

export const config = { path: "/*" };
