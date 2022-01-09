export default async (req, res) => {
  const value = await easily_broken.get(req.url.slice(1), {type: "json"});
  return value;
}

