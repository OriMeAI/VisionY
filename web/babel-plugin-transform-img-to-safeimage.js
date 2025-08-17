module.exports = function ({ types: t }) {
    return {
      visitor: {
        JSXOpeningElement(path) {
          const tagName = path.node.name;
          if (t.isJSXIdentifier(tagName) && tagName.name === "img") {
            tagName.name = "SafeImage";
          }
        },
        JSXClosingElement(path) {
          const tagName = path.node.name;
          if (t.isJSXIdentifier(tagName) && tagName.name === "img") {
            tagName.name = "SafeImage";
          }
        }
      }
    };
  };
  