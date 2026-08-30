-- Build: 3dcef763160429c566ec286c97a644a2
local M = {}

function M.clamp(value, minimum, maximum)
  return math.max(minimum, math.min(maximum, value))
end

return M
