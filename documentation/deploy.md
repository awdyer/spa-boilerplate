# Create and set up bucket for website hosting
aws s3 mb s3://www.awdyer.com
aws s3 website s3://www.awdyer.com --index-document index.html --error-document error.html

# Deploy website
aws s3 sync --acl public-read --sse --delete dist s3://www.awdyer.com
# view at www.awdyer.com.s3-website-ap-southeast-2.amazonaws.com

# Automated deployment
aws s3 sync --acl public-read --sse --delete dist s3://www.awdyer.com

aws configure set preview.cloudfront true   # Currently required while cloudfront command is in preview
aws cloudfront create-invalidation --distribution-id E16WSRI2RM3NMP --paths 'index.html'