require 'json'
require 'mini_magick'

def lambda_handler(event:, context:)

  base_img = 'default.png'
  image = MiniMagick::Image.open(base_img)
  image.combine_options do |conf|
    config.fill '#333333'
    config.gravity 'center'
    config.pointsize 65
    config.draw "text 0.0 'Hello World!!!'"
  end
  image.write "output.png"

  {
    statusCode: 200,
    body: {
      message: "Hello World!"
    }.to_json
  }
end
