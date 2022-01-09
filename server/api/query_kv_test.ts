export default async (req, res) => {
  const url = "http://192.168.208.206:8081/api" + req.url;
  const response = await fetch(url, {method: "POST"});
  return response.json();
}

